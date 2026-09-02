# pyrefly: ignore [missing-import]
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen2.5:7b")

response = llm.invoke("Hello introduce yourself")

print(response.content)
