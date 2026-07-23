from fastapi import APIRouter, Depends
from app.models.chat import ChatRequest, ChatResponse
from app.services.chat_service import process_chat
from app.core.dependencies import get_conversation_manager
from app.conversation.manager import ConversationManager

# create the router
router = APIRouter()

@router.post('/chat', response_model=ChatResponse)
def chat(
    request: ChatRequest,
    manager: ConversationManager = Depends(get_conversation_manager)):
    return process_chat(request, manager)
