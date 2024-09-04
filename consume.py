from settings import KAFKA_TOPIC
from kafka_object import consumer

from fastapi import APIRouter, Depends, WebSocket

consume_router = APIRouter(prefix="/v1", tags=["consume"])

@consume_router.websocket("/ws/commentary")
async def consume_commentary(websocket: WebSocket):
    await websocket.accept()
    
    for message in consumer:
        await websocket.send_json(message.value)
