import os
from functools import lru_cache

import chromadb
from sentence_transformers import SentenceTransformer

from config import (
    CHROMA_DIR,
    COLLECTION,
    DEEPSEEK_BASE_URL,
    DEEPSEEK_MODEL,
    EMBED_MODEL,
    RERANK_MODEL,
    USE_RERANK,
)

SYSTEM_PROMPT = (
    "Você é um assistente especialista em Git. Responda à pergunta usando "
    "SOMENTE o contexto fornecido. Se a resposta não estiver no contexto, "
    "diga que não encontrou na base. Ao final, cite os arquivos usados."
)


@lru_cache(maxsize=1)
def _embedder() -> SentenceTransformer:
    return SentenceTransformer(EMBED_MODEL)


@lru_cache(maxsize=1)
def _reranker():
    from sentence_transformers import CrossEncoder

    return CrossEncoder(RERANK_MODEL)


@lru_cache(maxsize=1)
def _llm():
    from openai import OpenAI

    key = os.getenv("DEEPSEEK_API_KEY")
    if not key:
        raise RuntimeError("Defina DEEPSEEK_API_KEY no arquivo rag/.env")
    return OpenAI(api_key=key, base_url=DEEPSEEK_BASE_URL)


def _collection():
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    try:
        return client.get_collection(COLLECTION)
    except Exception as exc:
        raise RuntimeError("Índice não encontrado. Rode: python rag/index.py") from exc


def buscar(query, nivel=None, categoria=None, k=8, top=4):
    qemb = _embedder().encode([query], normalize_embeddings=True).tolist()
    where = {}
    if nivel:
        where["nivel"] = nivel
    if categoria:
        where["categoria"] = categoria
    col = _collection()
    res = col.query(
        query_embeddings=qemb,
        n_results=k,
        **({"where": where} if where else {}),
    )
    docs = res["documents"][0]
    metas = res["metadatas"][0]
    if USE_RERANK and len(docs) > 1:
        try:
            scores = _reranker().predict([(query, d) for d in docs])
            order = sorted(range(len(docs)), key=lambda i: -float(scores[i]))
            docs = [docs[i] for i in order]
            metas = [metas[i] for i in order]
        except Exception:
            pass
    return [{"texto": d, "meta": m} for d, m in zip(docs[:top], metas[:top])]


def responder(query, nivel=None, categoria=None):
    trechos = buscar(query, nivel=nivel, categoria=categoria)
    contexto = "\n\n---\n\n".join(t["texto"] for t in trechos)
    resp = _llm().chat.completions.create(
        model=DEEPSEEK_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Contexto:\n{contexto}\n\nPergunta: {query}"},
        ],
    )
    answer = resp.choices[0].message.content
    fontes = sorted({t["meta"]["arquivo"] for t in trechos})
    return answer, fontes
