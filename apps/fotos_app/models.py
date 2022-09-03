from django.db import models

# Create your models here.
class  Photo(models.Model):

    image= models.ImageField(null=True, blank=True, upload_to='img/biblioteca', help_text='Seleccione una imagen para mostrar')
    descripcion=models.TextField()

    def __str__(self):
        return self.descripcion

class Revistas(models.Model):

    image = models.ImageField(null=True, blank=True, upload_to='img/tapaRevista', help_text='Seleccione una imagen para mostrar')
    titulo = models.CharField(max_length=255)
    link = models.CharField(max_length=255)



    





