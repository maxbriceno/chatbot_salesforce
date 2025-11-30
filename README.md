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

## System Architecture

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

## BE & App Architecture

Used feature first architecture to refactor the FastAPI `app` into modules. All choices have been made by abstraction, separation of interest and dependecy injection means.

```bash
- \src 
  |
  - \app
    |
    - \collection
    - \index
    - \llm
    - query_engine
  |  
  - \ingestion
  - \ui
```
  


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
This setup and installation guide shoudl be independent of the specific OS (Linux, MacOS, etc.)
### 1. Install python (3.10+ Recommended)
Windows:
```bash
python --version
```
Linux:
```bash
python3 --version
```
If python is not installed, download it from official site:
https://www.python.org/downloads/
### 2. Create .venv
From root directory `/chatbot_salesforce` create a venv:
```bash
py -m venv .venv
```
Move to the `.venv\Scripts` created directory and activate the virtual environment accordingly to your Host OS.
On Windows:
```bash
cd .venv\Scripts
Activate.ps1
``` 
On Linux:
```bash
cd .venv/Scripts
activate
```
### 3. Install dependencies
From the .venv move back to the project root directory and install project dependencies from requirements.txt file:
```bash
cd <your_path>\chatbot_salesforce
pip install -r requirements.txt
```
### 4. Run run_script.py from root project dir
On Windows:
```bash
py run_script.py
```
On Linux:
```bash
python3 run_script.py
```