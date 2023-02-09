from django.urls import path
from . import views


urlpatterns = [
    path('api/todos', views.todolist),
    path('api/todos/<int:pk>', views.todolist_detail),
]
