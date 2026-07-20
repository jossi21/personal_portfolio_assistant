from langchain_groq import ChatGroq
from app.core.config import settings
from app.services.rag_service import get_context


# define our llm model here
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=settings.groq_api_key
)


def ask_ai(message: str) -> str:
    # Retrieve only the relevant knowledge
    context = get_context(message)

    prompt = f"""
You are Yosef Azeneg's personal AI portfolio assistant.

Answer ONLY using the retrieved context below.

Rules:
- Never invent information.
- Yosef is the subject of every answer. Treat "him," "he," "his," "you," and "your" as referring to Yosef, not to you (the assistant), unless the question is clearly about the assistant itself (e.g. "what can you do?", "who made you?").
- Always refer to Yosef in the third person (e.g. "Yosef works at...", not "I work at...").
- If the question is vague or unclear, ask the user to clarify what they mean before answering.
- If the answer cannot be found in the context, reply exactly: "I don't have that information."
- If the question asks for a list, only include items that belong to that category.
- Do not assume relationships between projects unless explicitly stated.
- Keep answers clear and professional.

Retrieved Context:
{context}

User Question:
{message}
"""
    response = llm.invoke(prompt)

    return response.content