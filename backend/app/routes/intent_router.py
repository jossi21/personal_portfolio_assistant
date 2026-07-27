from app.models.chat import ChatRequest
from app.models.agent import AgentType
from app.models.route import RouteResult
from app.models.language import Language


LANGUAGE_CODE_MAP = {
    "english": Language.ENGLISH,
    "አማርኛ": Language.AMHARIC,
    "ትግርኛ": Language.TIGRINYA,
    "afaan oromoo": Language.AFAN_OROMO,
    "soomaali": Language.SOMALI,
}


class IntentRouter:
    """
    Routes a user request to the appropriate agent.
    """

    def route(self, request: ChatRequest) -> RouteResult:
        message = request.message.lower().strip()

        # Direct language selection (from a pill click)
        if message in LANGUAGE_CODE_MAP:
            return RouteResult(
                agent_type=AgentType.LANGUAGE,
                language=LANGUAGE_CODE_MAP[message].value,
            )

        # Generic "show me the language options" trigger
        if message == "change language":
            return RouteResult(
                agent_type=AgentType.LANGUAGE,
                language=None,
            )

        # Greeting
        if message in {"hi", "hello", "hey"}:
            return RouteResult(agent_type=AgentType.GREETING)

        # Typed natural-language requests (user typing "change to amharic" etc.)
        if (
            "language" in message
            or "change language" in message
            or "english" in message
            or "amharic" in message
            or "tigrigna" in message
            or "tigrinya" in message
            or "oromo" in message
            or "somali" in message
        ):
            language = None

            if "english" in message:
                language = Language.ENGLISH
            elif "amharic" in message or "አማርኛ" in message:
                language = Language.AMHARIC
            elif "tigrinya" in message or "tigrigna" in message or "ትግርኛ" in message:
                language = Language.TIGRINYA
            elif "oromo" in message or "afaan" in message:
                language = Language.AFAN_OROMO
            elif "somali" in message or "soomaali" in message:
                language = Language.SOMALI

            return RouteResult(
                agent_type=AgentType.LANGUAGE,
                language=language.value if language else None,
            )

        # Contact
        if (
            "contact" in message
            or "email" in message
            or "whatsapp" in message
            or "telegram" in message
            or "github" in message
        ):
            return RouteResult(agent_type=AgentType.CONTACT)

        # Resume
        if "resume" in message or "cv" in message:
            return RouteResult(agent_type=AgentType.RESUME)

        # Portfolio
        if (
            "project" in message
            or "portfolio" in message
            or "skill" in message
            or "experience" in message
        ):
            return RouteResult(agent_type=AgentType.PORTFOLIO)

        # Default RAG
        return RouteResult(agent_type=AgentType.RAG)