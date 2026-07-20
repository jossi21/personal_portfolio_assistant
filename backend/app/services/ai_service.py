from langchain_groq import ChatGroq
from app.core.config import settings
from app.services.rag_service import get_context
from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
)

from langchain_groq import ChatGroq


from app.core.config import settings

from app.services.rag_service import get_context

from app.services.chat_utils import (
    GREETING_RESPONSE,
    THANKS_RESPONSE,
    is_greeting,
    is_thanks,
)



# Initialize LLM

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=settings.groq_api_key,
)



def ask_ai(message: str) -> str:
    """
    Complete AI pipeline:

    1. Handle simple conversations
    2. Retrieve context
    3. Generate answer using LLM
    """



    # Greeting shortcut
    if is_greeting(message):
        return GREETING_RESPONSE



    # Thanks shortcut
    if is_thanks(message):
        return THANKS_RESPONSE



    # Retrieve knowledge
    context = get_context(message)



    system_prompt = f"""
You are Yosef Azeneg's personal AI portfolio assistant.

Your job is to answer questions about Yosef.

You can answer about:

- Projects
- Skills
- Experience
- Technologies
- Services
- Contact information
- How clients can work with Yosef


Rules:

1. Yosef is always the subject of the answer.

2. Refer to Yosef in third person:
Example:
Correct:
"Yosef built a Travel Planner Agent."

Incorrect:
"I built a Travel Planner Agent."


3. Use only the retrieved context.

4. Never invent information.

5. If the information is not available,
reply exactly:

"I don't have that information."


6. If someone asks how to work with Yosef,
explain available services from the context.


Retrieved Context:

{context}

"""



    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=message),
    ]



    response = llm.invoke(messages)



    return response.content