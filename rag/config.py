import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

VAULT_DIR = BASE_DIR.parent
CHROMA_DIR = BASE_DIR / "chroma"
COLLECTION = "git"

MAX_CHARS = int(os.getenv("CHUNK_MAX_CHARS", "1200"))
EMBED_MODEL = os.getenv("EMBED_MODEL", "BAAI/bge-m3")
RERANK_MODEL = os.getenv("RERANK_MODEL", "BAAI/bge-reranker-v2-m3")
USE_RERANK = os.getenv("USE_RERANK", "false").lower() in ("1", "true", "yes", "on")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
DEEPSEEK_MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
