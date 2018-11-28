from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/discovery/<device_name>/', consumers.ChatConsumer),
]