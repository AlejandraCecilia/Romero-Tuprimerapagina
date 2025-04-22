from django.db import models

class Especialidad(models.Model):
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    fecha_creation = models.DateField(null=True)
    
    def __str__(self):
        return f'{self.nombre} - {self.tipo}'
# Create your models here.
