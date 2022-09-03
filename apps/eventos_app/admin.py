from django.contrib import admin

from django.utils.safestring import mark_safe
from .models import Evento

# Register your models here.


class EventoAdmin(admin.ModelAdmin):
    list_display = ('name', 'modalidad', 'img')
    search_fields = ('name', 'modalidad',  'publicado')
    list_per_page = 25

    readonly_fields = ['evento_img']

    def evento_img(self,obj):
        return mark_safe('<a href="{0}"><img src="{0}" width="30%"></a>'.format(self.img.url))

admin.site.register(Evento, EventoAdmin)