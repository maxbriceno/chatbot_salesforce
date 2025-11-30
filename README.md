# Salesforce RAG Chatbot

## Overview

This project implements a **local chatbot** for querying Salesforce Commerce Cloud documentation.  
It is based on a **Retrieval-Augmented Generation (RAG)** architecture, using open-source tools and pre-trained models.

The chatbot can answer questions about:

- B2C Commerce Architecture
- Storefront Reference Architecture (SFRA)
- Composable Storefront
- Hybrid Storefront
- Salesforce Commerce Cloud APIs

### Example Questions

- Which API can I use to retrieve product stock?
- How can I extract the description of a category for a specific locale?
- What are the differences between Primary Instance Group and Secondary Instance Group?

## Architecture

The system follows a **RAG pipeline**:

1. **Document Ingestion**

   - PDFs or HTML pages of Salesforce documentation are parsed using `unstructured`.
   - Text is split into chunks 

2. **Embedding & Indexing**

   - Chunks are converted into embeddings using `HuggingFaceEmbedding (BGE-Small)`.
   - Embeddings are stored in **ChromaDB**, a local vector store.

3. **Retrieval & Generation**

   - User questions are sent to the **query engine** (`LlamaIndex`).
   - The engine retrieves the most relevant chunks from ChromaDB.
   - These chunks are fed as context to a **local LLM** (`qwen2.5:3b via Ollama`) to generate answers.

4. **Frontend / API**
   - The chatbot exposes a **FastAPI** endpoint (`/ask`).
   - Optional interfaces: **Streamlit UI** or **CLI** for local interaction.

## Tech Stack

| Component        | Purpose                                              |
| ---------------- | ---------------------------------------------------- |
| **Qwen-2.5:3B**  | Local LLM for generating answers                     |
| **LlamaIndex**   | Orchestrates RAG pipeline (retrieval)                |
| **ChromaDB**     | Local vector store for embeddings and chunk metadata |
| **unstructured** | Parsing PDFs / HTML documents to clean text chunks   |
| **FastAPI**      | Exposes `/ask` API endpoint for FE - BE interface    |
| **Streamlit**    | Lightweight UI for testing & demo                    |

## Setup Instructions (Windows / Local)

### 1. Install dependencies

```bash
pip install llama-index llama-index-embeddings-huggingface
pip install chromadb llama-index-vector-stores-chroma
pip install unstructured unstructured[pdf] pdfminer.six
pip install fastapi uvicorn
pip install streamlit  # optional for UI
```
