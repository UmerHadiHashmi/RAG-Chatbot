from app.services.vector_store import get_vector_store
from app.services.embeddings import get_embedding_function
from app.services.llm import generate_answer

def run_rag_pipeline(query: str) -> str:
    vectorstore = get_vector_store()
    docs = vectorstore.similarity_search(query, k=3)
    context = "\n".join([doc.page_content for doc in docs])
    return generate_answer(query, context)
