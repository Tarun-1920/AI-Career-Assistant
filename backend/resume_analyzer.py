from backend.gemini_client import ask_gemini
from backend.prompts import RESUME_ANALYZER_PROMPT

def analyze_resume(resume_text):

    messages = [
        {
            "role": "user",
            "content": RESUME_ANALYZER_PROMPT + "\n\nResume:\n\n" + resume_text
        }
    ]

    return ask_gemini(messages)