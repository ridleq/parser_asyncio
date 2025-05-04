import os
from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic.v1 import BaseSettings

load_dotenv()
config_path = os.getenv('CONFIG_PATH')


class DataBaseConfig(BaseModel):
    name: str
    user: str
    password: str
    host: str
    port: int


class Config(BaseModel):
    db: DataBaseConfig = None


def load_config(path: str = ".env") -> Config:
    from pathlib import Path

    class Settings(BaseSettings):
        DB_NAME: str
        DB_USER: str
        DB_PASSWORD: str
        DB_HOST: str
        DB_PORT: int

        class Config:
            env_file = Path(path)
            env_file_encoding = "utf-8"

    settings = Settings()
    return Config(
        db=DataBaseConfig(
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            name=settings.DB_NAME,
            password=settings.DB_PASSWORD,
            user=settings.DB_USER,
        )
    )


config = load_config(config_path)
