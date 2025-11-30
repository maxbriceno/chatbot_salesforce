# LLM locale (Ollama)
from llama_index.llms.ollama import Ollama

def set_llm():
        llm = Ollama(
            model="qwen2.5:3b",
            request_timeout=120,
            keep_alive="10m"
        )
        return llm