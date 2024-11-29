from langchain_ollama import OllamaLLM
from langchain_core.prompts.chat import ChatPromptTemplate
import subprocess
import atexit

process = subprocess.Popen(['ollama app.exe'])


template = """
Answer the question below.

Here is the conversatio history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("--------------------------------------")
    print("       WELCOME TO AI CHATBOT!         ")
    while True:
        print("--------------------------------------")
        user_input = input("You(q/quit): ")
        if user_input == "q".lower() or user_input == "quit".lower():
            break
        result = chain.invoke({"context":context, "question":user_input})
        print("AI: ", result)
        context += f"/n User: {user_input}/n AI: {result}"

def close_program():
    try:
        process.terminate()  
    except Exception as e:
        print(f"Error while closing the program: {e}")




if __name__ == "__main__":
    handle_conversation()