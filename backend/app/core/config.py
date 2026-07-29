from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Personal Portfolio Assistant"
    groq_api_key: str
    telegram_token: str
    web_chat_url: str = "http://localhost:3000"

    class Config:
        env_file = ".env"


settings = Settings()