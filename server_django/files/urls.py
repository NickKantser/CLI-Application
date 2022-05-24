from django.urls import path
from . import views

urlpatterns = [
    path('stat/', views.stat, name='stat'),
    path('read/', views.read, name='read'),
]
