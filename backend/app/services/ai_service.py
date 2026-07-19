from langchain_groq import ChatGroq
from app.core.config import settings
from app.services.knowledge_service import load_knowledge


# define our llm model here
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=settings.groq_api_key
)


def ask_ai(message: str)-> str:
    knowledge = load_knowledge()

    prompt = f"""
You are Jossi's personal portfolio assistant.

Answer questions using only the information provided below.

If the information is not available, say:
"I don't have that information."

Personal Information:

{knowledge}

User Question:

{message}
"""
    response = llm.invoke(prompt)

    return response.content