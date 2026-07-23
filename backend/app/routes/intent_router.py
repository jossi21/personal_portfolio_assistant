from enum import Enum
from app.models.chat import ChatRequest

class AgentType(str, Enum):
    """
    Represents the available agents in the system.
    """
    GREETING = "greeting"
    LANGUAGE = "language"
    PORTFOLIO = "portfolio"
    CONTACT = "contact"
    RESUME = "resume"
    RAG = "rag"


class IntentRouter:
    """
    Routes a user request to the appropriate agent
    """
    def route(self, request: ChatRequest)-> AgentType:
        """
        Determine which agent should handle the request
        """
        message = request.message.lower().strip()

        # Greeting
        if message in {"hi", "hello", "hey"}:
            return AgentType.GREETING

        # Language
        if "language" in message or "change language" in message or "english" in message or "amharic" in message :
            return AgentType.LANGUAGE

        # Resume
        if "resume" in message or "email" in message:
            return AgentType.RESUME

        # Contact 
        if "contact" in message or "email" in message or "whatsApp" in message or "telegram" in message:
            return AgentType.CONTACT

        # Portfolio
        if(
            "project" in message or
            "portfolio" in message or
            "skill" in message or
            "experience" in message
        ):
            return AgentType.PORTFOLIO

        # Default
        return AgentType.RAG
