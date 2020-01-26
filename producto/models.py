from django.db import models

# Create your models here.
class Producto(models.Model):  #lo segundo crear el modelo de la tabla
    nombre = models.CharField(blank=False, max_length=50, verbose_name='Nombre:', unique=True, help_text='Inglese el producto')
    precio = models.IntegerField(null=False, blank=False)
    descripcion = models.TextField(blank=True, max_length=100, verbose_name='Descripcion:', help_text='Ingrese Descripción del prodcuto')
    imagen = models.CharField(unique=False, max_length=100, verbose_name='Imagen Producto:', help_text='Ingrese URL de la imagen')
    fecha = models.DateField(verbose_name='Vencimiento:', help_text='Ingrese URL de la imagen')

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'