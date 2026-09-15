# Base de Conhecimento Git + RAG + MCP

Repositório com uma base de conhecimento de Git (em Markdown) e uma implementação de **RAG** (Retrieval-Augmented Generation) que expõe a base como um **servidor MCP** local. Assim, assistentes compatíveis com MCP (como o [opencode](https://opencode.ai)) podem consultar e responder perguntas sobre o conteúdo.

O motor do RAG fica na biblioteca **[personalrag](https://github.com/christian-s-barbosa/personalrag)**. Este repositório guarda apenas o **conteúdo** e a **configuração**.

## Estrutura

```
.
├── Basico/            # Fundamentos do Git (11 arquivos)
├── Intermediario/     # Temas intermediários (21 arquivos)
├── Avancado/          # Temas avançados (20 arquivos)
├── GitHub/            # Recursos do GitHub (8 arquivos)
├── Comando/           # Cheatsheets: Básicos, Intermediario e Avançado
├── index.md           # Índice geral da base
├── rag/               # Configuração do RAG (usa a lib personalrag)
│   ├── config.py      # Settings (vault, coleção, modelos)
│   ├── mcp_server.py  # Servidor MCP (tools buscar_git e responder_git)
│   ├── requirements.txt
│   └── .env.example
├── opencode.json      # Registro do MCP local no opencode
└── .gitignore
```

Cada arquivo da base tem um cabeçalho (frontmatter YAML) com metadados:

```yaml
---
titulo: Git commit
tipo: conceito
nivel: basico
categoria: Git
tags: [git, commit, versionamento, historico, staging]
resumo: "O que é um commit, como funciona, ciclo de vida dos arquivos..."
relacionados: ["Os três estados do Git", "Branches (Ramificações)"]
fonte: https://git-scm.com/docs/git-commit
---
```

## Como funciona

```
INDEXAÇÃO (offline)
arquivos .md → frontmatter + chunking → embeddings (bge-m3) → Chroma

CONSULTA (online)
pergunta → embedding → busca vetorial → (rerank opcional) → contexto
        → LLM (DeepSeek) → resposta com fontes
```

O RAG é exposto por um servidor **MCP** com duas ferramentas:

| Tool | O que faz |
| --- | --- |
| `buscar_git` | Retorna os trechos mais relevantes da base |
| `responder_git` | Responde a pergunta usando os trechos + DeepSeek |

## Requisitos

- Python 3.10+
- Uma chave de API do [DeepSeek](https://platform.deepseek.com)
- (Opcional) opencode, para usar o MCP

## Instalação

```powershell
# 1. Criar o ambiente virtual
python -m venv rag/.venv

# 2. Instalar as dependências (inclui a biblioteca personalrag)
rag/.venv/Scripts/pip install -r rag/requirements.txt
```

Em Linux/macOS, use `rag/.venv/bin/pip` no lugar de `rag/.venv/Scripts/pip`.

## Configuração

Copie o arquivo de exemplo e coloque sua chave:

```powershell
Copy-Item rag/.env.example rag/.env
```

Edite `rag/.env`:

```dotenv
DEEPSEEK_API_KEY=sua_chave_aqui
```

> As demais opções (modelos, rerank, chunk) ficam em `rag/config.py`. O DeepSeek é usado apenas para a **geração**; os embeddings rodam localmente com o `bge-m3` (não precisa de chave).

## Indexação

Gera o índice vetorial a partir dos arquivos `.md`:

```powershell
rag/.venv/Scripts/python -m personalrag --config rag/config.py index
```

- Na primeira execução, baixa o modelo `bge-m3` (~2 GB).
- O índice fica em `rag/chroma/` (não versionado).
- **Rode novamente sempre que editar/adicionar arquivos na base.**

## Teste pela linha de comando

```powershell
rag/.venv/Scripts/python -m personalrag --config rag/config.py query "como desfazer o último commit já enviado?"
```

## Uso como MCP (opencode)

O arquivo `opencode.json` já registra o servidor:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "git-rag": {
      "type": "local",
      "command": ["rag/.venv/Scripts/python.exe", "rag/mcp_server.py"],
      "enabled": true
    }
  }
}
```

Passos:

1. Gere o índice (comando de Indexação acima).
2. **Feche e reabra o opencode** para carregar o MCP.
3. As tools `buscar_git` e `responder_git` ficarão disponíveis.

> O caminho no `command` é relativo à raiz do projeto. Se o opencode iniciar de outra pasta, use um caminho absoluto.

## Observações sobre memória

- O `bge-m3` usa ~3–4 GB de RAM.
- Com o reranker (`use_rerank=True`), o pico sobe para ~6–8 GB.
- Em máquinas com pouca RAM, mantenha `use_rerank=False` ou use um reranker menor (`rerank_model="BAAI/bge-reranker-base"`).

## Personalização

As opções ficam em `rag/config.py` (dataclass `Settings`):

| Campo | Para que serve |
| --- | --- |
| `embed_model` | Modelo de embeddings (multilíngue) |
| `rerank_model` | Modelo de rerank |
| `use_rerank` | Liga/desliga o rerank |
| `chunk_max_chars` | Tamanho máximo de cada chunk |
| `metadata_fields` | Campos do frontmatter indexados |
| `llm_model` | Modelo de geração (`deepseek-chat` ou `deepseek-reasoner`) |
| `top_k` / `top_n` | Quantos recuperar / quantos enviar ao LLM |

## O que não é versionado

Veja o `.gitignore`: `rag/.venv/`, `rag/chroma/`, `rag/.env` e `__pycache__/`.
