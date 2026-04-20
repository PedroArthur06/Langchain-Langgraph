from langchain_ollama import ChatOllama
from rich import print

model = ChatOllama(model="llama3.2")

response = model.invoke("Hello, how are you?")
print(response)
