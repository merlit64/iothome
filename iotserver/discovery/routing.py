from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/discovery/discovery/', consumers.ChatConsumer),
]