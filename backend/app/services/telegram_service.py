import requests
from app.core.config import settings

class TelegramService:
    def send_message(
            self, chat_id: str, message: str
    ):
        url = (
            f"https://api.telegram.org/"
            f"bot{settings.telegram_token}/sendMessage"
        )

        payload = {
            "chat_id" : chat_id,
            "text": message
        }

        response = requests.post(
            url, json=payload
        )
        return response.json()
