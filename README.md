# 🧠 KnowFlow AI  
*A Retrieval-Augmented Generation (RAG) Chatbot for Your Documents*  

KnowFlow AI lets you **upload PDFs, DOCX, or TXT files** and ask natural-language questions about their content.  
It combines **OpenAI embeddings**, **FAISS vector search**, and **GPT-4o reasoning** inside a **Streamlit UI**.

---

## 🚀 Features
✅ Upload and parse PDF, DOCX, or TXT  
✅ Generate OpenAI `text-embedding-3-large` vectors  
✅ Store vectors locally using FAISS for semantic retrieval  
✅ Query your documents with GPT-4o grounded answers  
✅ Citations of retrieved chunks (“Sources”)  
✅ Lightweight Streamlit interface — runs locally in minutes  

---

## 🧱 Architecture
```text
User Upload → Text Extraction → Chunking
        ↓
OpenAI Embeddings → FAISS Vector Store
        ↓
Retriever (Top-k Chunks)
        ↓
GPT-4o → Context-aware Answer + Sources
        ↓
Streamlit UI


---

## 🗂️ Folder Structure


knowflow-ai/
│
├── app/
│   ├── __init__.py
│   ├── config.py          # Keys and paths
│   ├── utils.py           # Extraction + chunking
│   ├── retriever.py       # Embedding + FAISS
│   ├── generator.py       # GPT-4o answer logic
│   └── main.py            # Streamlit interface
│
├── data/
│   ├── raw/               # Uploaded files
│   └── processed/         # FAISS index + chunks
│
├── .env                   # OPENAI_API_KEY=sk-...
├── requirements.txt
└── README.md


---

## ⚙️ Installation

```bash
git clone https://github.com/<your-username>/knowflow-ai.git
cd knowflow-ai
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

Create a `.env` file:

```bash
OPENAI_API_KEY=sk-your-key
```

---

## ▶️ Run the App

```bash
streamlit run app/main.py
```

Then open: [http://localhost:8501](http://localhost:8501)

---

## 🧪 Usage

1. Upload a PDF/DOCX/TXT file in the sidebar.
2. Wait for “✅ Document indexed successfully.”
3. Type a question in the input box and click **Ask**.
4. Read your GPT-4o-generated, source-grounded answer.

---

## 💡 Example Query

> **Question:** What AI tools did Ashish use in his latest work experience?
>
> **Answer:**
> Ashish used RAG pipelines with FAISS/Pinecone, FastAPI, LLM APIs, and semantic search.
>
> **Sources:**
> [1] Resume_AKonagalla_AI.pdf (chunk 2)

---

## 🧩 Tech Stack

| Layer      | Tools                           |
| ---------- | ------------------------------- |
| UI         | Streamlit                       |
| Embeddings | OpenAI `text-embedding-3-large` |
| Vector DB  | FAISS (local)                   |
| LLM        | GPT-4o                          |
| Framework  | LangChain (for FAISS wrapper)   |
| Parsing    | PyMuPDF, docx2txt               |

---

## 🔒 Notes

* Only embeddings + answers are processed via OpenAI APIs.
* FAISS index and documents remain **local** to your machine.
* For free/offline demos, swap to SBERT embeddings instead.

---

## ☁️ Deployment (Optional)

Deploy easily on **Railway**, **Render**, or **Hugging Face Spaces**:

```bash
railway up   # or render.yaml / spaces app
```

---

## 🧾 License

MIT License © 2025 Ashish Konagalla

---

## ✨ Acknowledgements

* [LangChain](https://www.langchain.com) for vector utilities
* [Streamlit](https://streamlit.io) for rapid UI
* [OpenAI](https://openai.com) for embeddings + LLM API
* [FAISS](https://github.com/facebookresearch/faiss) for vector search

````

---
