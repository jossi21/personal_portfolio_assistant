from fastapi import APIRouter
from app.models.chat import ChatRequest, ChatResponse
from app.services.chat_service import process_chat
# create the router
router = APIRouter()

@router.post('/chat', response_model=ChatResponse)
def chat(request: ChatRequest):
    return process_chat(request)
