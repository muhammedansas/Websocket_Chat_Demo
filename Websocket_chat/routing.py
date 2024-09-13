from django.urls import path
from . import consumers  # Import the WebSocket consumer


websocket_urlpatterns = [
    path('ws/chat/', consumers.ChatConsumer.as_asgi()),  # WebSocket route
]