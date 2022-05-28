from django.urls import path
from . import views

urlpatterns = [
    path('stat/', views.StatView.as_view(), name='stat'),
    # path('stat/', views.stat, name='stat'),
    # path('read/', views.read, name='read'),
    path('read/', views.ReadView.as_view(), name='read'),
]
