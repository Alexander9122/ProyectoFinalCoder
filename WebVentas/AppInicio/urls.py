from django.urls import path
from AppInicio import views

urlpatterns = [

path('', views.inicio, name="Inicio"),
]
