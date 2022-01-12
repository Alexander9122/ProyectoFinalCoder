from django.urls import path
from AppTecno import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
#inicio de la app
path('tecnologia', views.tecnologia, name="Tecnologia"),

#Urls laptops
path('laptopRegistro',views.laptopRegistro, name="LaptopRegistro"),
path('leerLaptops',views.leerLaptops,name="LeerLaptops"),
path('eliminarLaptop/<numero_para_borrar>/',views.eliminaLaptop,name="EliminarLaptop"),
path('modificarLaptop/<numero_para_editar>/',views.modificarLaptop,name="ModificarLaptop"),
path('buscarLaptop/', views.buscarLaptop),
#Urls Views laptop
path('laptops',views.Laptoplist.as_view(),name='Laptops'),
path(r'^nuevo$', views.LaptopCreacion.as_view(), name='New'),
path(r'^editar/(?P<pk>\d+)$', views.LaptopModificar.as_view(), name='Edit'),
path(r'^borrar/(?P<pk>\d+)$', views.LaptopEliminar.as_view(), name='Delete'),

#Urls Celulares
path('celularesRegistro',views.celularesRegistro, name="CelularesRegistro"),
path('leerCelulares',views.leerCelulares,name="LeerCelulares"),
path(r'^editarCel/(?P<pk>\d+)$', views.CelularModificar.as_view(), name='EditCel'),
path('eliminarCelular/<numero_para_borrar>/',views.eliminaCelular,name="EliminarCelular"),
path('buscarCelular/', views.buscarCelular),

#Urls Televisores
path('televisoresRegistro',views.televisoresRegistro, name="TelevisoresRegistro"),
path('leerTelevisores',views.leerTelevisores,name="LeerTelevisores"),
path(r'^editarTel/(?P<pk>\d+)$', views.TelevisorModificar.as_view(), name='EditTel'),
path('eliminarTelevisor/<numero_para_borrar>/',views.eliminaTelevisor,name="EliminarTelevisor"),
path('buscarTelevisor/', views.buscarTelevisor),
]
