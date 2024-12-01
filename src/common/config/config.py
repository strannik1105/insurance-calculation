from pydantic_settings import BaseSettings

from utils.utils import Singleton


class AbstractConfig(BaseSettings):
    pass


class Config(AbstractConfig, Singleton[AbstractConfig]):
    HOST: str = "0.0.0.0"
    PORT: int = 8000
