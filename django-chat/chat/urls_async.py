from django.urls import path
from chat import views_async

websocket_urlpatterns = [
    path('ws/<slug:room_name>/', views_async.ChatConsumer.as_asgi())
]