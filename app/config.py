import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

    EMBEDDING_MODEL = "text-embedding-3-large"
    CHAT_MODEL = "gpt-4o"

    DATA_RAW = "data/raw"
    DATA_PROCESSED = "data/processed"
    FAISS_INDEX = os.path.join(DATA_PROCESSED, "faiss_index")

settings = Settings()

