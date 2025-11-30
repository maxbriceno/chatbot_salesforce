from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

def build_index():
    #* 1 - Leggi cartella input docs
    reader = SimpleDirectoryReader(input_dir="docs")
    documents = reader.load_data(show_progress=True, num_workers=1)
    #* 2 - Crea il client chroma - default to path="./chroma"
    chroma_client = chromadb.PersistentClient()
    chroma_collection = chroma_client.get_or_create_collection(name="sf_docs")
    #*3  - # Legge i documenti Salesforce (HTML, PDF, ecc.)
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    #* 4 - Embedding model
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    #* 5 - Costruzione indice
    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context,
        embed_model=embed_model
    )
    index.storage_context.persist()
    print("Index successfully created!")

if __name__ == "__main__":
    build_index()