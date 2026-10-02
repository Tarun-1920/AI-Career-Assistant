import os
from dotenv import load_dotenv
from google import genai

from backend.prompts import SYSTEM_PROMPT

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY was not found. Check your .env file."
    )

# Create Gemini client
client = genai.Client(api_key=api_key)


def ask_gemini(messages):
    try:
        # Start with system prompt
        conversation = SYSTEM_PROMPT + "\n\n"

        # Add chat history
        for message in messages:
            role = message.get("role", "user")
            content = message.get("content", "")

            if role == "user":
                conversation += f"User: {content}\n"
            else:
                conversation += f"Assistant: {content}\n"

        # Send request to Gemini
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=conversation
        )

        if not response.text:
            return "Gemini returned an empty response."

        return response.text

    except Exception as e:
        print(f"Gemini API Error: {type(e).__name__}: {e}")
        raise