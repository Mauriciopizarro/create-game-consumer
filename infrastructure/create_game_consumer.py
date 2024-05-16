from infrastructure.rabbit_consumer import RabbitConsumer
import json
import requests
from config import settings


class CreateGameListener(RabbitConsumer):

    topic = "game_started"

    def process_message(self, channel, method, properties, body):
        event = json.loads(body)
        players = event["players"]
        game_id = event["id"]
        url = f"{settings.GAME_SERVICE_URL}/game/create"
        requests.post(url=url, json={
            "game_id": game_id,
            "players": players
        })
