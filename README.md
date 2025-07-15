This is a Retrieval-Augmented Generation (RAG) chatbot using FastAPI, Chroma for vector storage, and Gemini 2.0 Flash LLM.

## Tech Stack
- **FastAPI**: API backend
- **ChromaDB**: Vector store
- **MiniLM-L6-v2**: Embeddings
- **Gemini Flash**: Language Model

## How to Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
