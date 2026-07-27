from app.services.telegram_service import TelegramService


telegram = TelegramService()


response = telegram.send_message(
    chat_id="7166954672",
    message="Hello from TelegramService"
)

print(response)