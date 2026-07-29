from app.models.chat import ChatResponse
from app.models.channel import ChannelMessage
from app.models.state import ConversationStateModel


class PortfolioAgent:

    def handle(
        self,
        request: ChannelMessage,
        state: ConversationStateModel,
    ) -> ChatResponse:

        return ChatResponse(
            session_id=state.session_id,
            answer="Portfolio information is coming soon.",
            language=state.language.value,
        )