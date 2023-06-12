from django.urls import path
from . import views

#lista que contiene funciones
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about,  name='blog-about'),
]

