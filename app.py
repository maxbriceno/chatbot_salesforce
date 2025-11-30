from fastapi import FastAPI
import chromadb
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.llms.ollama import Ollama
from pydantic import BaseModel
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

app = FastAPI()


# Load Chroma index default path="./chroma"
chroma_client = chromadb.PersistentClient()
chroma_collection = chroma_client.get_collection("sf_docs")

vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
index = VectorStoreIndex.from_vector_store(
    vector_store=vector_store,
    embed_model=embed_model
    )

# LLM locale (Ollama)
llm = Ollama(
    model="qwen2.5:3b",
    request_timeout=120,
    keep_alive="10m"
)

query_engine = index.as_query_engine(
    llm=llm,
    reponse_mode= "compact")

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask(q: Question):
    response = query_engine.query(q.question)
    return {"answer": str(response)}