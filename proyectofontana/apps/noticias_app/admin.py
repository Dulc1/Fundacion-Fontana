from django.contrib import admin
from .models import  categorias, noticia,comentarios

# Register your models here.

admin.site.register(categorias)
admin.site.register(noticia)
admin.site.register(comentarios)
