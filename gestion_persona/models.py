from django.db import models

# Create your models here.
class Persona(models.Model):
    dni = models.IntegerField(primary_key=True, null=False)
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=False)
    fecha_entrada = models.DateField(null=False)
    telefono = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    direccion = models.CharField(max_length=100, null=False)
    habitacion_nro = models.IntegerField(null=False)
#    habitacion_disponible = models.CharField(null=False, max_length=3)
    fecha_salida = models.DateField(null=False)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format (self.dni, self.nombre, self.apellido, self.fecha_entrada, self.telefono, self.email, self.direccion, self.habitacion_nro, self.fecha_salida)
    
