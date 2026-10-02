import json

from backend.gemini_client import ask_gemini
from backend.prompts import JOB_MATCHER_JSON_PROMPT


def analyze_job_match(resume_text, job_description):

    messages = [
        {
            "role": "user",
            "content": f"""
{JOB_MATCHER_JSON_PROMPT}

Resume:

{resume_text}

Job Description:

{job_description}
"""
        }
    ]

    response = ask_gemini(messages)

    response = response.strip()

    if response.startswith("```"):
        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

    return json.loads(response)