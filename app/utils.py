import os
import fitz      
import docx2txt

def extract_text(file_path: str) -> str:
    """Extract plain text from PDF, DOCX, or TXT."""
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        text = ""
        with fitz.open(file_path) as pdf:
            for page in pdf:
                text += page.get_text("text")
        return text

    elif ext == ".docx":
        return docx2txt.process(file_path)

    elif ext == ".txt":
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()

    else:
        raise ValueError(f"Unsupported file type: {ext}")


def clean_text(text: str) -> str:
    """Basic cleanup — remove extra spaces and blank lines."""
    return " ".join(text.split())


def chunk_text(text: str, chunk_size: int = 800, overlap: int = 100):
    """Split text into overlapping chunks for embedding."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks
