from unicodedata import category
from urllib import request
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from .models import noticia, comentarios,categorias
from apps.eventos_app.models import Evento
from django.contrib.auth.models import User
from django.http.response import Http404
from .forms import FormComment
from django.contrib.auth.decorators import login_required


def inicio(request):
    
    lista_noticias = noticia.objects.all().order_by('-id')[:3]
    lista_eventos = Evento.objects.all().order_by('-id')[:3]
    lista_user = User.objects.all()
    context = {
        "noticias": lista_noticias,
        "eventos": lista_eventos,
        "Usuarios": lista_user
    }
    return render(request, 'contenido_inicio.html', context)


def nosotros(request):
    return render(request, 'nosotros.html')


def biblioteca(request):
    return render(request, 'biblioteca.html')


def noticias(request):
    lista_categorias = categorias.objects.all()
    lista_noticias = noticia.objects.all().order_by('-id')
    context = {
        "categorias":lista_categorias,
        "noticias": lista_noticias
    }
    return render(request, 'noticias.html', context)


def noticiaDetalle(request, id):
    try:
        noticia = noticia.objects.get(id=id)
        lista_comentarios = comentarios.objects.filter(aprobado=True)
    except noticia.DoesNotExist:
        raise Http404('La Noticia solicitada no existe')\
    
    form = FormComment()
    
    if (request.method == "POST") and (request.user.id != None):
        form = FormComment(request.POST)
        if form.is_valid():
            comment = comentarios(
                autor_id = request.user.id,
                cuerpo_comentario=form.cleaned_data["cuerpo_comentario"],
                noticia=noticia
            )
            comment.save()
            return redirect("Noticia", id=noticia.id)

    context = {
        "form":form,
        "noticia": noticia,
        "comentarios": lista_comentarios
    }
    return render(request, 'noticiasdetalle.html', context)

def categoriaDetail(request, id):

    try:
        lista_categorias = categorias.objects.all()
        categoria = categorias.objects.get(id = id)
        noticias = noticia.objects.filter(categorias = id)
        lista_comentarios = comentarios.objects.filter(aprobado=True)
    except noticia.DoesNotExist:
        raise Http404('La Noticia solicitada no existe')\
    
    form = FormComment()
    
    if (request.method == "POST") and (request.user.id != None):
        form = FormComment(request.POST)
        if form.is_valid():
            print("Validacion Exitosa")

            comment = comentarios(
                autor_id = request.user.id,
                cuerpo_comentario=form.cleaned_data["cuerpo_comentario"],
                noticia=noticia
            )
            comment.save()
            return redirect("Noticia")

    context = {
        "categori":categoria,
        "categorias":lista_categorias,
        "form":form,
        "noticias": noticias,
        "comentarios": lista_comentarios
    }
    return render(request, 'noticias.html', context)


@login_required
def commentAproved(request, id):
    try:
        comentario = comentarios.objects.get(id=id)
    except comentarios.DoesNotExist:
        raise Http404("Inexistente")

    comentario.aprpove()
    return redirect("Noticia", id=comentario.noticia.id)