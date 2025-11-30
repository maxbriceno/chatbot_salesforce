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

## System Requirements
- Windows 10 or later (or Linux)
- macOS 14 Sonoma oer later
- 4-cores cpu (8-cores recommended)
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
This setup and installation guide should be independent of the specific OS (Linux, MacOS, etc.) but when required specific instructions are provided.

### 0. Install Ollama + qwen2.5:3b 
1. Install Ollama runtime for local LLMs
On Windows:
- Donwload installer at official site: https://ollama.com/download/windows
- Follow steps
On Linux:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
2. Test Ollama installation:
```bash
ollama --version
```
This command should print somithing similar.
```bash
PS C:\Users\user> ollama --version
ollama version is 0.13.0
```
3. Pull the desider model `qwen2.5:3b` 
```bash
ollama pull qwen2.5:3b
```
4. Check with command:
```bash
ollama list
```
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

## Note
The run_script.py uses a personal logger created to showcase the benifits of a Singleton and a Modular reusable logger module. Enjoy it.