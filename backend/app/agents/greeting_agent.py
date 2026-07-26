from app.models.chat import ChatRequest, ChatResponse
from app.services.chat_utils import GREETING_RESPONSE, is_greeting
from app.models.state import ConversationStateModel
from app.models.language import Language



    # Handles greeting conversations.

class GreetingAgent:

    def handle(
        self,
        request: ChatRequest,
        state: ConversationStateModel
    ) -> ChatResponse:


        return ChatResponse(
            session_id=state.session_id,
            answer=GREETING_RESPONSE,
            language=state.language.value
        )