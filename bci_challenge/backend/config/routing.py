from channels.auth import AuthMiddlewareStack
from channels.routing import (
    ProtocolTypeRouter,
    URLRouter,
)

from bci_challenge.blinks import routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})
