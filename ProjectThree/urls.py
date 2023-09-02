"""
URL configuration for ProjectThree project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
#estas auth views no hay que crearlas, ya vienen en el sistema:
from django.contrib.auth import views as auth_views
#STATIC FILED DEVELOPMENT MODE (DEBUG TRUE):
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register/', user_views.registro, name='registro'),
    path('profile/', user_views.profile, name='perfil'),
    #template_name da la ruta donde debe buscar los templates. Por default busca en registration/login.html...
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name = 'entrar'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name= 'salir'),
    #despues de cliquear forgot password? te manda aca para q introduzcas tu email:
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    #te sale un mensaje que te mandaron un mail con un link para cambiar el password:
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    #pinchas en el link que recibis en el email y te lleva a poner el nuevo pswd y confirmarlo:
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), 
         name='password_reset_confirm'),
    #mensaje de exito de que el password ha sido reseteado:         
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), 
         name='password_reset_complete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)