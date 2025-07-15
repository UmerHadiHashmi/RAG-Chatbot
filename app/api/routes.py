from fastapi import APIRouter
from app.models.schemas import QueryRequest, QueryResponse
from app.services.rag import run_rag_pipeline

router = APIRouter()

@router.post("/chat", response_model=QueryResponse)
async def chat(request: QueryRequest):
    answer = run_rag_pipeline(request.query)
    return QueryResponse(response=answer)
