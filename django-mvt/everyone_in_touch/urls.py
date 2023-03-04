from django.urls import path
from . import views


urlpatterns = [
    path('', views.startpage, name='startpage'),
    path('homepage/', views.homepage, name='homepage'),
    path('login/', views.login_, name='login'),
    path('logout/', views.logout_, name='logout'),
    path('sign_up/', views.sign_up, name='sign_up'),

]
