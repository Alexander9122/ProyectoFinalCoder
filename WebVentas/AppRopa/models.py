from django.db import models

# Aca podemos generar las clases

# Clase Ropa para Hombres

class Hombre(models.Model):

    talle = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    precio = models.IntegerField()

    def __str__(self):

        return f"Talle:\n {self.talle} Marca:\n {self.marca} Color:\n {self.color} Precio:\n {self.precio}"

# Clase Ropa para Mujer

class Mujer(models.Model):

    talle = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    precio = models.IntegerField()

    def __str__(self):

        return f"Talle:\n {self.talle} Marca:\n {self.marca} Color:\n {self.color} Precio:\n {self.precio}"

# Clase Ropa para Niños

class Niños(models.Model):

    talle = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    precio = models.IntegerField()

    def __str__(self):

        return f"Talle:\n {self.talle} Marca:\n {self.marca} Color:\n {self.color} Precio:\n {self.precio}"


