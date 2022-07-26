from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup", "good morning", "good afternoon", "good evening", "good day"):
        return "Good day, valued Guest!"

    if user_message in ("who are you?", "who are you?"):
        return "I am Angel the Bot! I inform Hotel Guests if it is meal time and collect their orders!"

    if user_message in ("meal times?", "meal times", "meal time", "schedule"):
        return "Breakfast: 7 AM - 8 AM \n Lunch: 12 PM - 1 PM \n Dinner: 6 PM - 7 PM"
    
    return "I'm sorry, I don't understand."

    