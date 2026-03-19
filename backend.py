from langgraph.graph import START,END, StateGraph
from typing import TypedDict, Annotated, List
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import BaseMessage,HumanMessage, SystemMessage


load_dotenv()


llm= ChatOpenAI()

SYSTEM_PROMPT = SystemMessage(content=(
    "You are FinLit Rep4® Bot, a financial literacy assistant. "
    "Format ALL of your responses using HTML. "
    "Use tags like <p>, <strong>, <em>, <ul>, <ol>, <li>, <br>, and <h4> where appropriate. "
    "When using <ul>, <ol> add padding left 20px for the list items. "
    "Do NOT include <html>, <head>, or <body> tags — only the inner content HTML. "
    "Keep responses clear and well-structured."
    "there are tools the user can use, when it is specified that they are using a tool guide the conversation to completing that tool's goal"
))


class Chatstate(TypedDict):
    messages: Annotated[List[BaseMessage],add_messages]
    tool: str

def chat_node(state:Chatstate):
    tool = state.get("tool")
    tool_prompt = []
    if tool:
        tool_prompt = [
            SystemMessage(content=f"Help me {tool}.")
        ]
    messages= [SYSTEM_PROMPT] + tool_prompt + state['messages']
    response= llm.invoke(messages)
    return {"messages":[response]}

checkpointer= InMemorySaver()

graph = StateGraph(Chatstate)

graph.add_node('chat_node',chat_node)

graph.add_edge(START,'chat_node')
graph.add_edge('chat_node', END)

chatbot= graph.compile(checkpointer=checkpointer)
