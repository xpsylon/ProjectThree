from django.urls import path
from . import views

#lista que contiene funciones
urlpatterns = [
    path('', views.home, name='casa-blog'),
    path('about/', views.about,  name='sobre-el-blog'),
]

