from typing import Any

from app.conversation.manager import ConversationManager
from app.channels.web.adapter import WebAdapter
from app.channels.telegram.adapter import TelegramAdapter
from app.channels.whatsapp.adapter import WhatsAppAdapter


class ChannelGateway:

    def __init__(
        self,
        manager: ConversationManager
    ):
        self.manager = manager

        self.adapters = {
            "web": WebAdapter(),
            "telegram": TelegramAdapter(),
            "whatsapp": WhatsAppAdapter(),
        }


    def handle_channel(
        self,
        request: Any,
        channel: str
    ):

        adapter = self.adapters.get(channel)

        if not adapter:
            raise ValueError(
                f"Unsupported channel: {channel}"
            )


        # Channel format -> AI format
        message = adapter.parse_message(
            request
        )


        # AI processing
        response = self.manager.handle(
            message
        )


        # AI format -> Channel format
        return adapter.format_response(
            response
        )