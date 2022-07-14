from django.urls import path
from . import views

urlpatterns = [
    #path('register/', views.register),
    path('register/', views.temp_register),
    path('login/', views.temp_login),
]
