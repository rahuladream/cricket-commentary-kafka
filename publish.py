from kafka_object import producer
from kafka.errors import KafkaError
from settings import KAFKA_TOPIC
from models import Commentary
from fastapi import APIRouter, Depends, HTTPException, Request, Response

publish_router = APIRouter(prefix="/v1", tags=["publish"])

@publish_router.post('/publish_commentary')
async def publish_commentary(commentary: Commentary):
    try:
        producer.send(KAFKA_TOPIC, {"commentary": commentary.commentary})
        producer.flush()
        
        return {"status": "Commentary Published"}
    except KafkaError as e:
        raise HTTPException(status_code=500, detail=str(e))
