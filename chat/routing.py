
from django.urls import re_path
# we user re_path due to the limitation we have in normal urls routing
from . import consumers
# fro
websocket_urlpatterns = [
    re_path('ws/socket-server/', consumers.ChatConsumer.as_asgi())
]