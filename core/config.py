from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Trading API"
    broker_api_url: str = "https://postman-echo.com"
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
