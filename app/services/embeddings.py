from langchain.embeddings import HuggingFaceEmbeddings
from app.core.config import settings

def get_embedding_function():
    return HuggingFaceEmbeddings(model_name=settings.EMBEDDING_MODEL)
