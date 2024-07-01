from django.db import models

class Estudiante(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    dni = models.CharField(max_length=8, unique=True)
    nombre = models.CharField(max_length=50)
    apepat = models.CharField(max_length=50)
    apemat = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    estado = models.CharField(max_length=1)