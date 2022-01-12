from django.db import models

# Create your models here.
#MODELO de accesorios del hogar blancos 
class Blanco(models.Model):
    marca = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=60)
    color = models.CharField(max_length=30)
    plazas = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.marca},{self.descripcion},{self.color},{self.plazas},{self.precio}"    

#MODELO de cocinas
class Cocinas(models.Model):
    marca = models.CharField(max_length=60)
    color = models.CharField(max_length=30)    
    canti_hornallas = models.IntegerField()
    def __str__(self):
        return f"{self.marca},{self.color},{self.canti_hornallas}" 

#MODELO de electrodmesticos 
class Electrodomesticos(models.Model):
    tipo = models.CharField(max_length=60) 
    marca = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)
    color = models.CharField(max_length=30) 
    voltage = models.IntegerField()     

    def __str__(self):
        return f"{self.tipo},{self.marca},{self.descripcion},{self.color},{self.color},{self.voltage}"
         