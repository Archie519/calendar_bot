from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# ✅ Load environment variables from .env file
load_dotenv()

# ✅ Get API keys from environment
api_key = os.getenv("GOOGLE_API_KEY")
calendar_id = os.getenv("GOOGLE_CALENDAR_ID")

app = FastAPI()

class UserInput(BaseModel):
    user_input: str

@app.post("/chat")
def chat_handler(user_input: UserInput):
    # Placeholder: here you would call your Google Calendar logic using the API key and calendar ID
    return {
        "response": f"📅 Got it! You said: {user_input.user_input}",
        "api_key": api_key,          # just for verification; remove in production
        "calendar_id": calendar_id   # just for verification; remove in production
    }
