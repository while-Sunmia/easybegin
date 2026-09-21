from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os


load_dotenv()  # Load environment variables from .env file
print(os.getenv("OPENAI_API_KEY"))

@tool
def introduce_yourself() -> str:
    """Introduce yourself to the user."""
    return "I am an AI-powered calculator. I can perform basic arithmetic operations like addition, subtraction, multiplication, and division. You can ask me to calculate expressions or just chat with me if you like !"
def calculator(a: float, b: float) -> str:
    """Perform basic arithmetic operations on two numbers."""
    print("Calculator activated!")
    return f"Sum of {a} and {b}: {a + b}, Difference of {a} and {b}: {a - b}, Product of {a} and {b}: {a * b}, Quotient of {a} and {b}: {a / b if b != 0 else 'undefined'}"


def main():
    model = ChatOpenAI(temperature=0)

    tool = [calculator, introduce_yourself]  # List of tools to be used by the agent
    agent_executor = create_react_agent(model, tool)

    print("Heyy Welcome! I am your AI Calculator. **Type 'exit' to quit.**")
    print("You can ask me to perform calculations or chat with me. ")
    print("For example, you can ask 'What is 2 + 2?' or 'Tell me a joke'")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "exit":
            print("Sad to see you leave. Sayonara then!")
            break
        
        print("\n Calculator: ", end="")
        for chunk in agent_executor.stream({"messages": [HumanMessage(content=user_input)]}):
            if "agent" in chunk and "messages" in chunk["agent"] :
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="") #ts is so that msg response by agent comes bit by bit and not all at once.

        print()

if __name__ == "__main__":
    main()



            
             
