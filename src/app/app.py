from fastapi import FastAPI
from pydantic import BaseModel

from src.app.query_engine.query_engine_handler import get_query_engine

app = FastAPI()

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask(q: Question):
    response = get_query_engine().query(q.question)
    return {"answer": str(response)}