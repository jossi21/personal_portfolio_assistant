from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Personal Portfolio Assistant"
    groq_api_key: str
    telegram_token: str

    class Config:
        env_file = ".env"


settings = Settings()