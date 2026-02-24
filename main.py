from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_core.messages import HumanMessage
from backend import chatbot

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
def hello():
    return {"message": "hello world"}

class ChatRequest(BaseModel):
    tool: str = ""
    message: str = ""
    thread_id: str = "default"

@app.post("/chat")
def chat(req: ChatRequest):
    result = chatbot.invoke(
        {"messages": [HumanMessage(content=req.message)]},
        config={"configurable": {"thread_id": req.thread_id}},
    )
    response = result["messages"][-1].content
    return {"message": response}