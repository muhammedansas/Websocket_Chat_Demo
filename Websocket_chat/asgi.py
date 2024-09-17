"""
ASGI config for Websocket_chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import Websocket_chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Websocket_chat.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),                             # Handles traditional HTTP requests
    'websocket': AuthMiddlewareStack(                           # Handles WebSocket connections
        URLRouter(
            Websocket_chat.routing.websocket_urlpatterns        # WebSocket routing
        )
    ),
})
