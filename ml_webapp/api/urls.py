from django.urls import path
from . import views

urlpatterns = [
    path('apiview/', views.Authspotify),
]
