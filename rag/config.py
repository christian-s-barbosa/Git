from pathlib import Path

from dotenv import load_dotenv

from ragcore import Settings

HERE = Path(__file__).resolve().parent
load_dotenv(HERE / ".env")

settings = Settings(
    vault_dir=str(HERE.parent),
    collection="git",
    index_dir=str(HERE / "chroma"),
    use_rerank=False,
)
