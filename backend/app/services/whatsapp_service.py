import requests

from app.core.config import settings
from app.models.chat import ActionType


class WhatsAppService:

    BASE_URL = "https://graph.facebook.com/v23.0"


    def send_message(
        self,
        phone_number: str,
        message: str,
        actions: list | None = None,
    ):

        url = (
            f"{self.BASE_URL}/"
            f"{settings.phone_number_id}/messages"
        )

        headers = {
            "Authorization": (
                f"Bearer {settings.whatsapp_token}"
            ),
            "Content-Type": "application/json",
        }


        payload = self.build_payload(
            phone_number,
            message,
            actions
        )


        response = requests.post(
            url,
            headers=headers,
            json=payload,
        )

        print("Status:", response.status_code)
        print("Response:", response.text)

        return response.json()



    def build_payload(
        self,
        phone_number: str,
        message: str,
        actions: list | None
    ):

        if not actions:
            return self.text_payload(
                phone_number,
                message
            )


        buttons = []

        for action in actions[:3]:

            if action.type in (
                ActionType.BUTTON,
                ActionType.LANGUAGE,
            ):

                buttons.append(
                    {
                        "type": "reply",
                        "reply": {
                            "id": action.value,
                            "title": action.label[:20],
                        },
                    }
                )


        if not buttons:
            return self.text_payload(
                phone_number,
                message
            )


        return {
            "messaging_product": "whatsapp",
            "to": phone_number,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                    "text": message
                },
                "action": {
                    "buttons": buttons
                }
            }
        }



    def text_payload(
        self,
        phone_number,
        message
    ):

        return {
            "messaging_product": "whatsapp",
            "to": phone_number,
            "type": "text",
            "text": {
                "body": message
            }
        }