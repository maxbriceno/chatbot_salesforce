
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import VectorStoreIndex

from src.app.collection.chroma_handler import get_chroma_collection

def create_index():
    vector_store = ChromaVectorStore(chroma_collection=get_chroma_collection())
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

    index = VectorStoreIndex.from_vector_store(
        vector_store=vector_store,
        embed_model=embed_model
        )
    return index