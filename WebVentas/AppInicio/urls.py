from django.urls import path
from AppInicio import views

#Import Login
from django.contrib.auth.views import LogoutView


urlpatterns = [

path('', views.inicio, name="Inicio"),
path('about', views.about, name="About"),

#URLs Login
path('login',views.login_request, name='Login'),
path('registro',views.register, name='Registro'),
path('logout',LogoutView.as_view(template_name='AppInicio/logout.html'),name='Logout'),
path('editarPerfil',views.editarPerfil, name="EditarPerfil"),
]
