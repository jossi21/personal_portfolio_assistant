from fastapi import APIRouter, Depends, HTTPException
from app.conversation.manager import ConversationManager
from app.core.dependencies import get_conversation_manager
from app.models.state import ConversationStateModel

# create the router
router = APIRouter()

# define the endpoint
@router.get("/conversation/{session_id}",
            response_model=ConversationStateModel)
def get_conversation(
    session_id: str,
    manager: ConversationStateModel = Depends(get_conversation_manager)
):
    state = manager.state_manager.get(session_id)

    if not state:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found"
        )
    return state
