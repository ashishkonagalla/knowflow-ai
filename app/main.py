import sys, os

# Force Python to treat the project root ("knowflow") as a package path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import streamlit as st
from app.utils import extract_text, clean_text, chunk_text
from app.retriever import create_vector_store, load_vector_store
from app.generator import generate_answer
from app.config import settings


st.set_page_config(page_title="KnowFlow AI", page_icon="🧠", layout="wide")

st.title("🧠 KnowFlow AI")
st.caption("Ask questions about your documents using RAG (Retrieval-Augmented Generation).")

# Ensure folders exist
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

# --- Sidebar ---
st.sidebar.header("📂 Document Upload")
uploaded_file = st.sidebar.file_uploader("Upload a file (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    raw_path = os.path.join("data/raw", uploaded_file.name)
    with open(raw_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.sidebar.success(f"✅ File uploaded: {uploaded_file.name}")

    # Extract and process text
    st.write("🔄 Extracting and embedding text...")
    text = extract_text(raw_path)
    text = clean_text(text)
    chunks = chunk_text(text)

    # Create FAISS vector store
    create_vector_store(chunks)
    st.success("✅ Document indexed successfully! You can now ask questions.")

# --- Main Chat Section ---
st.markdown("### 💬 Ask a Question")
query = st.text_input("Enter your question:")
ask_button = st.button("Ask")

if ask_button and query.strip():
    with st.spinner("Retrieving relevant chunks..."):
        vs = load_vector_store()
        retrieved = vs.similarity_search(query, k=3)

    with st.spinner("Generating answer..."):
        answer = generate_answer(query, retrieved)

    st.markdown("### 🧠 Answer:")
    st.write(answer)
