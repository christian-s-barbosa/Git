import re

import chromadb
import frontmatter
from sentence_transformers import SentenceTransformer

from config import CHROMA_DIR, COLLECTION, EMBED_MODEL, MAX_CHARS, VAULT_DIR


def _iter_markdown():
    for path in sorted(VAULT_DIR.rglob("*.md")):
        rel = path.relative_to(VAULT_DIR)
        if "rag" in rel.parts:
            continue
        if any(part.startswith(".") for part in rel.parts):
            continue
        yield path


def _split_secao(secao):
    if len(secao) <= MAX_CHARS:
        return [secao]
    partes, buf = [], ""
    for p in re.split(r"\n\s*\n", secao):
        if len(buf) + len(p) > MAX_CHARS and buf:
            partes.append(buf.strip())
            buf = p
        else:
            buf = (buf + "\n\n" + p).strip()
    if buf:
        partes.append(buf)
    return partes


def chunks_do_arquivo(path):
    post = frontmatter.load(path)
    meta = post.metadata
    rel = path.relative_to(VAULT_DIR).as_posix()
    resultado = []
    for secao in re.split(r"(?m)^(?=## )", post.content):
        secao = secao.strip()
        if not secao:
            continue
        for pedaco in _split_secao(secao):
            heading = (
                pedaco.splitlines()[0].lstrip("#").strip()
                if pedaco.startswith("#")
                else ""
            )
            breadcrumb = f"[{meta.get('categoria', '')} > {meta.get('titulo', '')} > {heading}]"
            resultado.append(
                {
                    "texto": f"{breadcrumb}\n{pedaco}",
                    "meta": {
                        "arquivo": rel,
                        "titulo": str(meta.get("titulo", "")),
                        "nivel": str(meta.get("nivel", "")),
                        "categoria": str(meta.get("categoria", "")),
                        "tipo": str(meta.get("tipo", "")),
                        "tags": ",".join(meta.get("tags", [])),
                    },
                }
            )
    return resultado


def main():
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    try:
        client.delete_collection(COLLECTION)
    except Exception:
        pass
    col = client.create_collection(COLLECTION, metadata={"hnsw:space": "cosine"})

    docs, metas, ids = [], [], []
    for path in _iter_markdown():
        for i, c in enumerate(chunks_do_arquivo(path)):
            docs.append(c["texto"])
            metas.append(c["meta"])
            ids.append(f"{c['meta']['arquivo']}::{i}")

    print(f"Chunks gerados: {len(docs)}")

    model = SentenceTransformer(EMBED_MODEL)
    embeddings = model.encode(
        docs, normalize_embeddings=True, batch_size=32, show_progress_bar=True
    )

    for start in range(0, len(docs), 500):
        end = start + 500
        col.add(
            ids=ids[start:end],
            documents=docs[start:end],
            metadatas=metas[start:end],
            embeddings=embeddings[start:end].tolist(),
        )

    print(f"OK: {len(docs)} chunks na coleção '{COLLECTION}'.")


if __name__ == "__main__":
    main()
