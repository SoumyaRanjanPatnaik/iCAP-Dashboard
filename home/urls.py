from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send', views.send, name = 'ajax'),
    path('get', views.get, name = 'get')
]

