from app.models.chat import ChatResponse, Action, ActionType
from app.models.state import ConversationStateModel
from app.models.channel import ChannelMessage
from app.core.config import settings


class WelcomeAgent:

    def handle(
        self,
        request: ChannelMessage,
        state: ConversationStateModel
    ) -> ChatResponse:


        username = request.user_name

        greeting = (
            f"Hello {username} \n\n"
            if username
            else "Hello \n\n"
        )


        return ChatResponse(
            session_id=state.session_id,

            answer=(
                greeting +
                "Welcome to Jossi's Personal Assistant.\n\n"
                "I can help you learn about my projects, "
                "skills, experience, and contact information."
            ),

            actions=[

                Action(
                    label="Change Language",
                    type=ActionType.LANGUAGE,
                    value="change_language"
                ),

                Action(
                    label="Telegram Bot",
                    type=ActionType.LINK,
                    value="http://t.me/JossiAzBot"
                ),

                Action(
                    label="WhatsApp Bot",
                    type=ActionType.LINK,
                    value="https://wa.me/+251925553491"
                ),

                Action(
                    label="Continue Web Chat",
                    type=ActionType.LINK,
                    value=settings.web_chat_url
                )
            ]
        )