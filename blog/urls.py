from django.urls import path
from .views import PostListView
from . import views

#lista que contiene funciones
urlpatterns = [
    #path('', views.home, name='casa-blog'), #LA ANTIGUA FUNCTION-BASED VIEW
    path('', PostListView.as_view(), name='casa-blog'),
    path('about/', views.about,  name='sobre-el-blog'),
]
#we get error template doesn exist. By convention, Django searches for:
#<app>/<model>_<viewtype>.html
#blog/post_list.html