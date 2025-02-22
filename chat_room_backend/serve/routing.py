from django.urls import path
from serve.consumer import ChatConsumer


websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/<str:user_name>', ChatConsumer.as_asgi()),
]