from backend.gemini_client import ask_gemini

def chat_with_pdf(docs, question):

    context = ""

    for doc in docs:
        context += doc.page_content + "\n\n"

    messages = [
        {
            "role": "user",
            "content": f"""
Answer ONLY using this context.

Context:

{context}

Question:

{question}
"""
        }
    ]

    return ask_gemini(messages)