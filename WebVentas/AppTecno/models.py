from django.db import models

# Create your models here.
class Laptops(models.Model):

    marca = models.CharField(max_length=10)
    pulgadas = models.IntegerField()
    procesador = models.CharField(max_length=20)
    ram = models.CharField(max_length=5)
    precio = models.FloatField()

    def __str__(self):

        return f"ID:{self.id} MARCA:{self.marca} PULGADAS:{self.pulgadas} PROCESADOR:{self.procesador} RAM:{self.ram} PRECIO:{self.precio}"

class Celulares(models.Model):

    marca = models.CharField(max_length=10)
    compania = models.CharField(max_length=10)
    conectividad = models. CharField(max_length=3)
    memoria = models.CharField (max_length=6)
    precio = models.FloatField ()

    def __str__(self):

        return f"ID:{self.id} MARCA: {self.marca} COMPANIA: {self.compania} CONECTIVIDAD: {self.conectividad} MEMORIA: {self.memoria} PRECIO:{self.precio}"

class Televisores(models.Model):
    
    marca = models.CharField(max_length=10)
    pulgadas = models.IntegerField()
    resolusion = models.CharField(max_length=10)
    precio = models.FloatField()

    def __str__(self):

        return f"ID:{self.id} MARCA: {self.marca} PULGADAS: {self.pulgadas} RESOLUCION: {self.resolusion} PRECIO:{self.precio}"
