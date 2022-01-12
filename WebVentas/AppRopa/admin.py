from django.contrib import admin

# Register your models here.

from .models import *

#Desde aca podemos crear las opciones de hombre,mujer y niños en el usuario admin, para luego agregar los datos que queramos

admin.site.register(Hombre)

admin.site.register(Mujer)

admin.site.register(Niños)
