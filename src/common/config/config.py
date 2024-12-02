from pydantic_settings import BaseSettings

from utils.utils import Singleton


class AbstractConfig(BaseSettings):
    pass


class AppConfig(AbstractConfig, Singleton[AbstractConfig]):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class PostgresConfig(AbstractConfig, Singleton[AbstractConfig]):
    POSTGRES_USER: str = "insurance_user"
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_DB: str = "insurance"
    POSTGRES_HOST: str = "postgres"
    POSTGRES_PORT: int = 5432


class KafkaConfig(AbstractConfig, Singleton[AbstractConfig]):
    KAFKA_HOST: str = "kafka"
    KAFKA_PORT: int = 9092
