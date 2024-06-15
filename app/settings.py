from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = Field("Shithead", env='APP_NAME')

    database_url: str = Field("sqlite:///app/data/db.sqlite")
    ACCESS_TOKEN_EXPIRE_MINUTES = 120

    class Config:
        env_file = '.env'


settings = Settings()
