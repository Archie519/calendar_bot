import os
from datetime import datetime, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define Google API scope
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Get service account key file path
SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_CLIENT_SECRET")

# Authenticate using service account
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Initialize Google Calendar API client
calendar_service = build('calendar', 'v3', credentials=credentials)

def get_available_slots():
    """Return dummy available time slots (replace with real logic later)"""
    return ["3:00 PM", "4:00 PM"]

def book_slot(slot_time, summary="AI Meeting"):
    """
    Book a 1-hour meeting on the calendar at the given slot_time.
    This version assumes UTC time for simplicity.
    """
    calendar_id = os.getenv("GOOGLE_CALENDAR_ID")

    # Example: parse "3:00 PM" into datetime object (optional logic needed here)
    # For now, just book at current UTC + 1 hour
    start_time = datetime.utcnow().replace(minute=0, second=0, microsecond=0)
    end_time = start_time + timedelta(hours=1)

    event = {
        'summary': summary,
        'start': {'dateTime': start_time.isoformat() + 'Z', 'timeZone': 'UTC'},
        'end': {'dateTime': end_time.isoformat() + 'Z', 'timeZone': 'UTC'},
    }

    # Call Google Calendar API to create the event
    calendar_service.events().insert(calendarId=calendar_id, body=event).execute()
    return "✅ Booking confirmed at " + start_time.strftime("%I:%M %p UTC")
