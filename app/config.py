from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGODB_DATABASE_URL: str
    MONGO_INITDB_DATABASE: str

    class Config:
        env_file = 'app/.env'
        env_file_encoding = 'utf-8'

settings = Settings()


