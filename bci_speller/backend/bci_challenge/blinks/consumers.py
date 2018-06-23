import logging

from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer

from .models import BCIDevice

logger = logging.getLogger(__name__)


class BCIConsumer(JsonWebsocketConsumer):
    def connect(self):
        self.device_group_name = None
        device_id = self.scope['url_route']['kwargs']['device_id']
        if BCIDevice.objects.filter(device_id=device_id).exists():
            self.device_group_name = f'bci_{device_id}'
            logger.info(f'Connecting to "{self.device_group_name}" group.')
            async_to_sync(self.channel_layer.group_add)(
                self.device_group_name,
                self.channel_name,
            )
            self.accept()
        else:
            logger.info(f'Device with id - "{device_id}" not found.')
            self.close()

    def disconnect(self, close_code):
        logger.info(
            f'Leaving "{self.device_group_name}" group with close code - '
            f'{close_code}.'
        )
        if self.device_group_name is not None:
            async_to_sync(self.channel_layer.group_discard)(
                self.device_group_name,
                self.channel_name,
            )

    def receive_json(self, content, **kwargs):
        logger.info(
            f'Receive data in group "{self.device_group_name}": {content}',
        )
        async_to_sync(self.channel_layer.group_send)(
            self.device_group_name,
            {
                'type': 'blink_message',
                'data': content,
            },
        )

    def blink_message(self, event):
        self.send_json(content={'data': event['data']})
