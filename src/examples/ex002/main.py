from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama
from rich import print

model = ChatOllama(model="llama3.2")

system_prompt = "Você é um pirata que está sempre bravo."
human_message = HumanMessage(content="opa! como você está?")
system_message = SystemMessage(content=system_prompt)

response = model.invoke([system_message, human_message])
print(response)
 