from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str
    feedback: str | None = None