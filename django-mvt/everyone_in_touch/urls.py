from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.login_, name='login'),
    path('logout/', views.logout_, name='logout'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('teachers/', views.TeacherListView.as_view(), name='teachers'),
    path('teachers/<int:pk>', views.TeacherDetailView.as_view(), name='teacher'),
    path('about_us/', views.about_us, name='about_us'),
]
