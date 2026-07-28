from fastapi import APIRouter, Depends
from app.services.channel_gateway import ChannelGateway
from app.core.dependencies import get_channel_gateway
from app.services.telegram_service import TelegramService

router = APIRouter(
    prefix="/telegram",
    tags=["Telegram"]
)

telegram_service = TelegramService()

@router.post("/webhook")
def telegram_webhook(
    data: dict,
    gateway: ChannelGateway = Depends(get_channel_gateway)
):
    response = gateway.handle_channel(
        data,
        "telegram"
    )

    # print(response)


    telegram_service.send_message(
        chat_id=response["chat_id"],
        message=response["message"],
        actions=response.get("actions")
    )


    return {
        "status": "sent"
    }