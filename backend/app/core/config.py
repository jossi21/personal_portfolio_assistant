from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Personal Portfolio Assistant"
    groq_api_key: str
    telegram_token: str
    web_chat_url: str = "http://localhost:3000"

    # Add WhatsApp fields
    whatsapp_token: str
    phone_number_id: str
    whatsapp_business_account_id: str
    verify_token: str

    class Config:
        env_file = ".env"


settings = Settings()