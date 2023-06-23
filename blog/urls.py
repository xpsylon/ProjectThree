from django.urls import path
from .views import PostListView, PostDetailView
from . import views

#lista que contiene funciones
urlpatterns = [
    #path('', views.home, name='casa-blog'), #LA ANTIGUA FUNCTION-BASED VIEW
    path('', PostListView.as_view(), name='casa-blog'),
    #usando la convencion de django para acceder a cada posteo se pasa el PK (primary key):
    path('post/<int:pk>/', PostDetailView.as_view(), name='detalle_posteo'),
    path('about/', views.about,  name='sobre-el-blog'),
]
#we get error template doesn exist. By convention, Django searches for:
#<app>/<model>_<viewtype>.html
#blog/post_list.html