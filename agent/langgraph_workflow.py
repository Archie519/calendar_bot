from agent.intent_parser import parse_user_intent
from agent.google_calendar import get_available_slots, book_slot

def langgraph_response(user_input):
    intent = parse_user_intent(user_input)

    if intent.get("action") == "check":
        return "Available slots: " + ", ".join(get_available_slots())

    elif intent.get("action") == "book":
        return book_slot(intent.get("time"))

    return "Sorry, I didn't understand."
