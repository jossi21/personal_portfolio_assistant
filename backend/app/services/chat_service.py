from app.models.chat import (
    ChatRequest,
    ChatResponse,
)
from app.services.ai_service import ask_ai

def process_chat(request: ChatRequest) -> ChatResponse:
    """
    Process incoming chat requests.

    Responsibilities:
    - Receive request data
    - Send message to AI service
    - Format response
    """

    answer = ask_ai(request.message)

    return ChatResponse(
        answer=answer
    )