import re

def parse_user_intent(user_input):
    # Example: "book a meeting tomorrow at 3 PM"
    intent = {}

    if "tomorrow" in user_input.lower():
        intent["date"] = "tomorrow"
    if "afternoon" in user_input.lower():
        intent["time"] = "3:00 PM"
    elif match := re.search(r"(\d{1,2})([:.]?\d{0,2})?\s?(AM|PM)", user_input, re.IGNORECASE):
        intent["time"] = match.group(0)

    intent["action"] = "book" if "book" in user_input.lower() else "check"
    return intent
