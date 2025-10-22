from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from app.config import settings
import os

def create_vector_store(chunks):
    """Embed text chunks and save them in a local FAISS index."""
    # Initialize embedding model
    embeddings = OpenAIEmbeddings(
        openai_api_key=settings.OPENAI_API_KEY,
        model=settings.EMBEDDING_MODEL
    )

    # Create FAISS vector store from chunks
    vectorstore = FAISS.from_texts(chunks, embeddings)

    # Ensure directory exists
    os.makedirs(settings.FAISS_INDEX, exist_ok=True)

    # Save index locally
    vectorstore.save_local(settings.FAISS_INDEX)
    print(f"✅ FAISS index saved to: {settings.FAISS_INDEX}")
    return vectorstore


def load_vector_store():
    """Load an existing FAISS index if it exists."""
    embeddings = OpenAIEmbeddings(
        openai_api_key=settings.OPENAI_API_KEY,
        model=settings.EMBEDDING_MODEL
    )
    return FAISS.load_local(settings.FAISS_INDEX, embeddings, allow_dangerous_deserialization=True)
