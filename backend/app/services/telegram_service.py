import requests
from app.core.config import settings
from app.models.chat import ActionType


class TelegramService:

    def send_message(
            self,
            chat_id: str,
            message: str,
            actions: list | None = None
    ):

        url = (
            f"https://api.telegram.org/"
            f"bot{settings.telegram_token}/sendMessage"
        )

        payload = {
            "chat_id": chat_id,
            "text": message
        }

        if actions:
            keyboard = []
            row = []

            for action in actions:
                button = None

                if action.type == ActionType.LINK:
                    if action.value.startswith("http"):
                        button = {
                            "text": action.label,
                            "url": action.value
                        }

                    elif action.value.startswith("mailto:"):
                        email = action.value.replace("mailto:", "")
                        button = {
                            "text": action.label,
                            "url": (
                                "https://mail.google.com/mail/"
                                f"?view=cm&fs=1&to={email}"
                            )
                        }


                    # handle language action type here
                elif action.type == ActionType.LANGUAGE:
                    button = {
                        "text": action.label,
                        "callback_data": (
                            f"language:{action.value}"
                        )
                    }


                if button:
                    row.append(button)
                    # when we have 2 buttons create a row
                    if len(row) == 2:
                        keyboard.append(row)
                        row = []

            # will take the full row
            if row:
                keyboard.append(row)


            if keyboard:

                payload["reply_markup"] = {
                    "inline_keyboard": keyboard
                }


        response = requests.post(
            url,
            json=payload
        )
        return response.json()