from settings import KAFKA_BROKER_URL, KAFKA_TOPIC

from kafka import KafkaProducer, KafkaConsumer
import json

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER_URL,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BROKER_URL,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="commentary-group",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)