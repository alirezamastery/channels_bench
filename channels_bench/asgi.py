import os

from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channels_bench.settings')
django_asgi_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter

from chat.websocket.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    'websocket': URLRouter(
        websocket_urlpatterns
    )
})