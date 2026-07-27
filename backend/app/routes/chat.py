from fastapi import APIRouter, Depends, Header
from app.models.chat import ChatRequest, ChatResponse
from app.services.channel_gateway import ChannelGateway
from app.core.dependencies import get_channel_gateway

router = APIRouter()


@router.post("/chat")
def chat(
    request: ChatRequest,
    channel: str =Header("web", alias="X-Channel"),
    gateway: ChannelGateway = Depends(get_channel_gateway)
):
    return gateway.handle_channel(request, channel)