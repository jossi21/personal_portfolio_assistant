from langchain_groq import ChatGroq
from app.core.config import settings
from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
)
from app.services.chat_utils import (
    GREETING_RESPONSE,
    THANKS_RESPONSE,
    is_greeting,
    is_thanks,
)
from app.prompts.system_prompt import get_system_prompt


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
    system_prompt = get_system_prompt(message)
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=message),
    ]
    response = llm.invoke(messages)


    return response.content