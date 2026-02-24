from langgraph.graph import START,END, StateGraph
from typing import TypedDict, Annotated, List
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import BaseMessage,HumanMessage


load_dotenv()


llm= ChatOpenAI()


class Chatstate(TypedDict):
    messages: Annotated[List[BaseMessage],add_messages]

def chat_node(state:Chatstate):
    messages= state['messages']
    response= llm.invoke(messages)
    return {"messages":[response]}

checkpointer= InMemorySaver()

graph = StateGraph(Chatstate)

graph.add_node('chat_node',chat_node)

graph.add_edge(START,'chat_node')
graph.add_edge('chat_node', END)

chatbot= graph.compile(checkpointer=checkpointer)
