from django.urls import path
from . import views

app_name = 'keny'

urlpatterns = [
    path('registeration', views.register, name='register'),
    path('login', views.user_login, name='user_login'),
]
