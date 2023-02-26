from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index),
    path('json_api/', views.json_index),
    path('', views.GetUsers.as_view()),
    path('homepage/', views.homepage),
    path('todos/', views.GetTodos.as_view()),
]
