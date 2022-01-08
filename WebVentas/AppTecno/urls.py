from django.urls import path
from AppTecno import views

urlpatterns = [

path('', views.inicio, name="Inicio"),
path('laptops',views.laptops, name="Laptops"),
path('celulares',views.celulares, name="Celulares"),
path('televisores',views.televisores, name="Televisores"),
path('correcto', views.correcto, name="Correcto"),
path('leerLaptops',views.leerLaptops,name="LeerLaptops"),
path('eliminarLaptop/<numero_para_borrar>/',views.eliminaLaptop,name="EliminarLaptop"),

]
