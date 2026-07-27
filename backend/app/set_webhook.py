# save as set_webhook.py
import requests

token = "8703025562:AAHv46JmsvTokRyeivl7FBBwb9t1xixus1U"
webhook_url = "https://humid-commode-showy.ngrok-free.app/telegram/webhook"

response = requests.post(
    f"https://api.telegram.org/bot{token}/setWebhook",
    json={"url": webhook_url}
)

print(response.json())