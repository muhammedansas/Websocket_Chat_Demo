import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Automatically accept WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Automatically handle WebSocket disconnection
        pass

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Echo the received message back to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))