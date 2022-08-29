from time import timezone
from django.shortcuts import render
from .models import noticia,categorias,comentarios
from django.http.response import Http404
#from django.http import HttpResponse


# Create your views here.
def inicio(request):
    texto = {'mensaje_texto': 'Esta es mi primer pagina :)'}
    ultimasnoticias = noticia.objects.all().order_by('creado').reverse()[:3]
    context ={
        'noticiasdestacadas':ultimasnoticias
    }
    return render(request, 'base.html',context)

def nosotros(request):
    return render(request, 'nosotros.html',{})

def Noticias(request):
    lista_noticias = noticia.objects.all().order_by('creado')
    context = {
        "noticias": lista_noticias,
    }
    return render(request, 'noticias.html',context)

def noticiasdetalle(request,id):
    try:
        datanoticia = noticia.objects.get(id=id)
        lista_comentarios = comentarios.objects.filter(aprobado=True)
    except noticia.DoesNotExist:
        raise Http404('La Noticia solicitada no existe')

    context = {
        "noticia": datanoticia,
        "comentarios":lista_comentarios
    }

    return render(request,'noticiasdetalle.html',context)