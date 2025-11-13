import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import Aplicaciones.geografica.routing  

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carros.settings')
django.setup()

# Configura la aplicación ASGI
application = ProtocolTypeRouter({
    # Maneja solicitudes HTTP normales
    "http": get_asgi_application(),

    # Maneja conexiones WebSocket
    "websocket": AuthMiddlewareStack(
        URLRouter(
            Aplicaciones.geografica.routing.websocket_urlpatterns
        )
    ),
})
