from app.models.chat import ChatResponse, ChatRequest
from app.services.ai_service import ask_ai
from app.models.state import ConversationStateModel
from app.models.language import LANGUAGE_NAMES



class RAGAgent:
    def handle(
        self, request: ChatRequest, state: ConversationStateModel
    ) -> ChatResponse:

        language_name = LANGUAGE_NAMES.get(
            state.language.value, "English"
        )

        answer = ask_ai(request.message, language_name)

        return ChatResponse(
            answer=answer,
            session_id=state.session_id,
        )