from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserInput(BaseModel):
    user_input: str

@app.get("/")
def home():
    return {"message": "✅ API is running!"}

@app.post("/chat")
def chat_handler(user_input: UserInput):
    return {"response": f"📅 Got it! You said: {user_input.user_input}"}
