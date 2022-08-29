from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import  categorias, noticia,comentarios

# Register your models here.

#admin.site.register(categorias)
#admin.site.register(noticia)
#admin.site.register(comentarios)

class CategoriasAdmin(admin.ModelAdmin):
    list_display= ('Nombre',)

admin.site.register(categorias)  

class NoticiasAdmin(admin.ModelAdmin):
    list_display= ('titulo', 'autor','img')
    search_fields= ('titulo', 'autor','creado', )
    
    list_per_page= 25

    readonly_fields=['noticia_img']

    def noticia_img(self, obj):
        return mark_safe (
            '<a href="{0}"><img src="{0}" width=300</a>'.format(self.img.url )
        )

admin.site.register(noticia,NoticiasAdmin)

class ComentariosAdmin(admin.ModelAdmin):
    list_display=('autor', 'cuerpo_comentarios','noticia','creado','aprobado')

    list_filter = ('aprobado', 'creado')

    search_fields = ('autor', 'cuerpo_comentario')

    actions= ['aprobar_comentarios']

    def aprobar_comentarios(self,request,queryset):
        queryset.update(aprobado=True)

admin.site.register(comentarios,ComentariosAdmin)
        
        