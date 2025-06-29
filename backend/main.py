# main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Global chat memory
chat_history = []

class UserInput(BaseModel):
    user_input: str

@app.post("/chat")
def chat_handler(user_input: UserInput):
    user_msg = user_input.user_input
    bot_msg = f"📅 Got it! You said: {user_msg}"

    chat_history.append({"user": user_msg, "bot": bot_msg})

    return {
        "response": bot_msg,
        "full_chat": chat_history
    }

@app.get("/")
def home():
    return {"message": "✅ API is running!"}

