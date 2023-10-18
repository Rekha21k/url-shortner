from django.urls import path
from .views import home, createShortURL, redirect

urlpatterns = [
    path('', home, name='home'),
    path('create/',createShortURL, name='createshortURL'),
    path('<str:short_id>/', redirect, name='redirect'),
] 
