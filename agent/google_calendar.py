import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_CLIENT_SECRET")

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

calendar_service = build('calendar', 'v3', credentials=credentials)

def get_available_slots():
    # Return dummy slots
    return ["3:00 PM", "4:00 PM"]

def book_slot(slot_time, summary="AI Meeting"):
    calendar_id = os.getenv("GOOGLE_CALENDAR_ID")
    from datetime import datetime, timedelta

    start_time = datetime.utcnow().replace(hour=15, minute=0).isoformat() + 'Z'
    end_time = (datetime.utcnow() + timedelta(hours=1)).isoformat() + 'Z'

    event = {
        'summary': summary,
        'start': {'dateTime': start_time, 'timeZone': 'UTC'},
        'end': {'dateTime': end_time, 'timeZone': 'UTC'}
    }

    calendar_service.events().insert(calendarId=calendar_id, body=event).execute()
    return "Booking confirmed!"
