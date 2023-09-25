from pydantic import BaseSettings

class AppConfig(BaseSettings):
    app_name: str = "My FastAPI App"
    debug: bool = False
    database_url: str

config = AppConfig()