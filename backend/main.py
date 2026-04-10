from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from chatbot import get_bot_response

app = FastAPI()

# ✅ CORS FIX (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "AI Chatbot Backend Running 🚀"}

@app.post("/chat")
def chat(message: Message):
    response = get_bot_response(message.text)
    return {"response": response}