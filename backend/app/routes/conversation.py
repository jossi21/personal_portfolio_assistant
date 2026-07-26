from fastapi import APIRouter, HTTPException
from app.conversation.state_manager import StateManager


router = APIRouter()

state_manager = StateManager()


@router.get("/conversation/{session_id}")
def get_conversation(session_id: str):

    state = state_manager.get(session_id)

    if not state:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found"
        )

    return {
        "session_id": state.session_id,
        "language": state.language,
        "history": state.history
    }