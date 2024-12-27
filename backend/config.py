import os
from pydantic import Field
from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    db_url: str = Field(..., env='postgresql://admin:admin123@fastapidb:5432')


settings = Settings()
