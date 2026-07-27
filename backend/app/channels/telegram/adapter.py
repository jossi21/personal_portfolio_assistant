from app.channels.base import ChannelAdapter
from app.models.channel import ChannelMessage


class TelegramAdapter(ChannelAdapter):

    def parse_message(self, data):

        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]

        return ChannelMessage(
            user_id=f"telegram:{chat_id}",
            channel="telegram",
            session_id=f"telegram:{chat_id}",
            message=text
        )


    def format_response(self, response):

        return {
            "chat_id": response.session_id.replace(
                "telegram:",
                ""
            ),
            "message": response.answer,
            "actions": response.actions
        }