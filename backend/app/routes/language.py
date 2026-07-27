from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.core.dependencies import get_conversation_manager
from app.conversation.manager import ConversationManager
from app.models.language import Language
from app.models.chat import ChatResponse, Action, ActionType
from app.services.language_response import get_greeting_response

router = APIRouter()

class LanguageRequest(BaseModel):
    session_id: str
    language: Language


@router.post("/language", response_model=ChatResponse)
def change_language(
    request: LanguageRequest,
    manager: ConversationManager = Depends(get_conversation_manager),
):
    state = manager.state_manager.get_or_create(request.session_id)
    state.language = request.language

    greeting = get_greeting_response(state.language)

    return ChatResponse(
        session_id=state.session_id,
        answer=greeting,
        actions=[
            Action(
                label="Change Language",
                type=ActionType.LANGUAGE,
                value="change language",
            ),
        ],
        language=state.language.value,
    )