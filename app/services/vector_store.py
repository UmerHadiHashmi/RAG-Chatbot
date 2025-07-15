from langchain_community.vectorstores import Chroma
from app.services.embeddings import get_embedding_function
from app.utils.loader import load_documents
from app.core.config import settings

def get_vector_store():
    embedding = get_embedding_function()
    return Chroma(
        collection_name="faq_collection",
        persist_directory=settings.PERSIST_DIRECTORY,
        embedding_function=embedding,
    )

# On startup / reindex
def initialize_vector_store():
    embedding = get_embedding_function()
    docs = load_documents(settings.DATA_PATH)
    Chroma.from_documents(
        documents=docs,
        embedding=embedding,
        persist_directory=settings.PERSIST_DIRECTORY,
        collection_name="faq_collection"
    )
