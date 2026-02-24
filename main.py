from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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

@app.post("/chat")
def chat(req: ChatRequest):
    if req.tool == "build-budget":
        response = "Let's build your college budget! ..."
    elif req.tool == "plan-purchase":
        response = "Let's plan a purchase! ..."
    elif req.tool == "check-credit":
        response = "Let's check your credit! ..."
    elif req.tool == "calculate-loan":
        response = "Let's calculate your loan! ..."
    elif req.tool == "debt-management":
        response = "Let's manage your debt! ..."
    elif req.tool == "export":
        response = "Exporting..."
    else:
        user_text = req.message
        response = f"You said: {user_text}"  # normal chat fallback
    return {"message": response}