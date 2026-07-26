from app.models.chat import ChatResponse, ChatRequest, Action, ActionType
from app.models.state import ConversationStateModel
from app.models.language import Language


class ContactAgent:
    """
    Handles contact-related requests.

    Returns contact information and clickable actions.
    """

    def handle(
        self,
        request: ChatRequest,
        state: ConversationStateModel
    ) -> ChatResponse:

        actions = [
            Action(
                label="Email",
                type=ActionType.LINK,
                value="mailto:azenegyosef@gmail.com"
            ),
            Action(
                label="LinkedIn",
                type=ActionType.LINK,
                value="https://www.linkedin.com/jossi21"
            ),
            Action(
                label="GitHub",
                type=ActionType.LINK,
                value="https://github.com/jossi21"
            ),
            Action(
                label="WhatsApp",
                type=ActionType.LINK,
                value="https://api.whatsapp.com/send?phone=251925553491"
            ),
            Action(
                label="Portfolio",
                type=ActionType.LINK,
                value="https://yosef-azeneg.vercel.app"
            )
        ]

        messages = {
            Language.ENGLISH:
                "You can contact Yosef through the following channels:",

            Language.AMHARIC:
                "ዮሴፍን በሚከተሉት መንገዶች ማግኘት ይችላሉ፦",

            Language.TIGRINYA:
                "ዮሴፍ ብትዕዛዞም መንገዲታት ክትረኽቦ ትኽእል፦",

            Language.AFAN_OROMO:
                "Yoseef karaa armaan gadiitiin qunnamuu dandeessu:",

            Language.SOMALI:
                "Waxaad Yosef kala xiriiri kartaa hababka soo socda:"
        }

        return ChatResponse(
            session_id=state.session_id,
            answer=messages.get(
                state.language,
                messages[Language.ENGLISH]
            ),
            actions=actions
        )