from backend.gemini_client import ask_gemini
from backend.prompts import INTERVIEW_PROMPT

def interview_response(chat_history):

    messages = [
        {
            "role": "user",
            "content": INTERVIEW_PROMPT
        }
    ]

    messages.extend(chat_history)

    return ask_gemini(messages)