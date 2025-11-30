import chromadb

def get_chroma_collection():
    chroma_client = chromadb.PersistentClient()
    chroma_collection = chroma_client.get_collection("sf_docs")
    return chroma_collection