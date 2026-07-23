from app.models.chat import ChatRequest, ChatResponse
from app.conversation.manager import ConversationManager

def process_chat(
        request: ChatRequest,
        manager: ConversationManager) -> ChatResponse:
    """
    Process incoming chat requests.

    Responsibilities:
    - Receive validated request data
    - Delegate conversation handling
    - Return formatted response
"""

    return manager.handle(request)