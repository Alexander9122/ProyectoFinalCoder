from django.urls import path
from AppHogar import views

urlpatterns = [
    path('hogar', views.hogar, name='Hogar' ),
    path('blanco', views.blanco, name='Blanco' ),
    path('cocinas',views.cocinas, name='Cocinas'),
    path('electrodomesticos', views.electrodomesticos, name='Electrodomesticos'),
    path('blancoForm', views.blancoForm, name='BlancoForm' ),
    path('cocinasForm', views.cocinasForm, name='CocinasForm' ),
    path('electrodomesticosForm', views.electrodomesticosForm, name='ElectrodomesticosForm' ),

    path('eliminarBlanco/<nombreBorrar>/', views.eliminarBlanco, name='EliminarBlanco' ),
    path('editarBlanco/<descripcionEditar>/', views.editarBlanco, name='EditarBlanco' ),

    

    path('leerBlancos', views.leerBlancos, name='LeerBlancos'),
    path('leerCocinas', views.leerCocinas, name='LeerCocinas'),
    path('leerElectrodomesticos', views.leerElectro, name='LeerElectrodomesticos'),

    

    












]