from django.db import models
from datetime import datetime
from django.utils import timezone


# Create your models here.
class Evento(models.Model):
    name = models.CharField(max_length=255)
    dia=models.DateTimeField()
    publicado=models.DateTimeField(auto_now=True)
    modalidad= models.CharField(max_length=100)
    detalles=  models.TextField()
    lugar= models.CharField(max_length=255)
    img=models.ImageField(null=True, blank=True, upload_to='img/eventos', help_text='Seleccione una imagen para mostrar')

    def publicarEvento(self):

        self.publicado= datetime.now()
        self.save()