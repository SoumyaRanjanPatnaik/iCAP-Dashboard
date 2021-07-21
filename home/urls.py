from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('attendance', views.attendence,name='attendence'),
    path('logs', views.logs,name='logs'),
    path('about', views.about,name='about'),
    path('send', views.send, name = 'ajax'),
    path('get', views.get, name = 'get')
]

