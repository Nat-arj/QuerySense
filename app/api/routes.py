from fastapi import APIRouter
from app.models.query_model import QueryRequest
from app.services.prompt_service import build_prompt
from app.services.ollama_service import call_llm
from app.storage.history import query_history

router = APIRouter()

@router.post("/optimize")
def optimize_query(data: QueryRequest):

    prompt = build_prompt(
        data.query,
        data.feedback
    )

    result = call_llm(prompt)

    if data.query:
        query_history.append(data.query)

    if data.feedback:
        query_history.append(data.feedback)

    return {
        "result": result,
        "history": query_history
    }

@router.get("/history")
def get_history():

    return {
        "history": query_history
    }