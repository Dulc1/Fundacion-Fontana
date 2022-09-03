from django.db import models
from datetime import datetime
from django.utils import timezone


# Create your models here.
class Evento(models.Model):
    organiza= models.ForeignKey( 'auth.User',on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    dia= models.DateTimeField(null=True)
    publicado = models.DateTimeField(blank=True, null=True)
    modalidad= models.CharField(max_length=100)
    detalles=  models.TextField()
    lugar= models.CharField(max_length=255)
    img= models.ImageField(null=True, blank=True, upload_to='img/eventos', help_text='Seleccione una imagen para mostrar')

    def publicarEvento(self):

        self.publicado= datetime.now()
        self.save()
    
    def comentariosAprobados(self):
        return self.comentarios.filter(aprobado=True)