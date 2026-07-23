from app.models.chat import ChatResponse, ChatRequest
from app.services.ai_service import ask_ai

class RAGAgent:
    """
    Agent responsible for answering questions using
    Retrieval-Augmented Generation (RAG).
    """

    def handle(self, request: ChatRequest)-> ChatResponse:
        """
        Process a chat request and return an AI-generated response.
        """
        answer = ask_ai(request.message)

        return ChatResponse(
            answer=answer
        )