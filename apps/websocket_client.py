import json
import ssl

from websocket import create_connection


class WebSocketClient:
    def __init__(self, socket_url):
        self.connection = create_connection(
            socket_url,
            sslopt={"cert_reqs": ssl.CERT_NONE},
        )

    def send_data(self, type_, amount, **kwargs):
        data = {
            'type': type_,
            'amount': amount,
            **kwargs,
        }
        self.connection.send(json.dumps(data))
