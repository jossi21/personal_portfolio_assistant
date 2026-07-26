from app.models.chat import ChatRequest, ChatResponse, Action, ActionType
from app.models.state import ConversationStateModel
from app.models.route import RouteResult
from app.services.language_response import (
    get_language_changed_response,
    get_select_language_response,
)

LANGUAGE_OPTIONS = [
    Action(label="English", type=ActionType.LANGUAGE, value="English"),
    Action(label="አማርኛ", type=ActionType.LANGUAGE, value="አማርኛ"),
    Action(label="ትግርኛ", type=ActionType.LANGUAGE, value="ትግርኛ"),
    Action(label="Afaan Oromoo", type=ActionType.LANGUAGE, value="Afaan Oromoo"),
    Action(label="Soomaali", type=ActionType.LANGUAGE, value="Soomaali"),
]


class LanguageAgent:
    """
    - If a specific language was resolved by the router (route.language),
      state.language has already been updated by ConversationManager,
      so we confirm the switch using a fixed, pre-written string
      in that language.
    - Otherwise (generic "change_language" trigger), show the options.
    """

    def handle(
        self,
        request: ChatRequest,
        state: ConversationStateModel,
        route: RouteResult,
    ) -> ChatResponse:

        if route.language:
            return ChatResponse(
                session_id=state.session_id,
                answer=get_language_changed_response(state.language),
                actions=[
                    Action(
                        label="Change Language",
                        type=ActionType.LANGUAGE,
                        value="change_language",
                    ),
                ],
                language=state.language.value,
            )

        return ChatResponse(
            session_id=state.session_id,
            answer=get_select_language_response(state.language),
            actions=LANGUAGE_OPTIONS,
            language=state.language.value,
        )