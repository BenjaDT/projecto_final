from django.db import models

# Create your models here.

class Provedor(models.Model):
    nombre = models.CharField(max_length=50)
    #el contacto es un numero de telefono
    contacto = models.IntegerField()

    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField(max_length=8)
    #fecha_de_precio es la fecha a la cual se le coloco el precio al producto
    fecha_de_precio = models.DateField(null=True)
    descripcion = models.CharField(max_length=500)
    provedor_id = models.ForeignKey(Provedor, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre
    

class Local(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    #el contacto es un numero de telefono de ventas
    contacto = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre