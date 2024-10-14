from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre_completo = models.CharField(max_length=50)
    peso = models.IntegerField()
    talla = models.IntegerField()

    def __str__(self):
        return (f'Usuario: {self.nombre_completo}')