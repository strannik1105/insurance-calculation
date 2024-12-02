import json

from kafka import KafkaClient as KafkaMigrateClient, KafkaProducer

from common.config.config import KafkaConfig
from common.kafka.messages import ActionMessage
from common.kafka.topics import KafkaTopicType


class KafkaClient:
    def __init__(self) -> None:
        config = KafkaConfig.get_instance()
        self._producer = KafkaProducer(
            bootstrap_servers=f"{config.KAFKA_HOST}:{config.KAFKA_PORT}"
        )

    def _send(self, topic: KafkaTopicType, msg: dict) -> None:
        self._producer.send(topic=topic.value, value=json.dumps(msg).encode("utf-8"))

    def send_log(self, log: ActionMessage) -> None:
        # вообще лучше через фабрики разруливать но пусть будет "dummy" реализация
        self._send(
            KafkaTopicType.ACTION_LOG,
            {"action": log["action"].value, "entity": log["entity"].value},
        )


class KafkaMigrator:
    def __init__(self) -> None:
        config = KafkaConfig.get_instance()
        self._client = KafkaMigrateClient(
            bootstrap_servers=f"{config.KAFKA_HOST}:{config.KAFKA_PORT}"
        )

    def migrate(self) -> None:
        self._client.add_topic(KafkaTopicType.ACTION_LOG.value)
