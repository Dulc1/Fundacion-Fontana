from time import timezone
from django.shortcuts import render, redirect
from .models import noticia,categorias,comentarios
from django.http.response import Http404
from django.conf import settings
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NoticiaForm, CommentarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import( CreateView)
from django.shortcuts import get_object_or_404

# Create your views here.
def inicio(request):
    #texto = {'mensaje_texto': 'Esta es mi primer pagina :)'}
    ultimasnoticias = noticia.objects.all().order_by('creado').reverse()[:3]
    context ={
        'noticiasdestacadas':ultimasnoticias
    }
    return render(request, 'contenido_inicio.html',context)

def nosotros(request):
    return render(request, 'nosotros.html',{})

def noticias(request):
    lista_noticias = noticia.objects.all().order_by('creado')
    context = {
        "noticias": lista_noticias,
        "MEDIA_ROOT": 'media/img/noticias/'
    }
    return render(request, 'noticias.html',context)

def noticiasdetalle(request,id):
    try:
        datanoticia = noticia.objects.get(id=id)
        lista_comentarios = comentarios.objects.filter(aprobado=True)
        print(lista_comentarios)
    except noticia.DoesNotExist:
        raise Http404('La Noticia solicitada no existe')

    #form=CommentarioForm()
    context = {
        "noticia": datanoticia,
        "comentarios":lista_comentarios,
        #"formulario":form,
        
       # "MEDIA_ROOT": 'media',
    }

    return render(request,'noticiasdetalle.html',context)

    

class CrearNoticiaView(CreateView, LoginRequiredMixin):
    login_url= '/login'
    #redirect_field_name='index_detail.html'

    form_class = NoticiaForm

    model = noticia


    def blog_categoria(request, categoria):
        posts = noticia.objects.filter(
            categories__name__contains=categoria
        ).order_by(
            'creado'
        )
        context = {
            "categoria": categoria,
            "posts": posts
        }
        return render(request, "blog_categoria.html", context)


@login_required
def post_publish(request, id):
    try:
        noticias =noticia.objects.get(id =id)
    except noticia.DoesNotExist:
        raise Http404('No existe la noticia')
    
    noticia.publish()
    return redirect('detalle-noticia', id=id)


@login_required
def comment_approve(request, id):
    try:
        comentarios =comentarios.objects.get(id =id)
    except comentarios.DoesNotExist:
        raise Http404('Comentario no existe')
    comentarios.approve()
    return redirect('detalle-noticia', id=comentarios.noticia.id)


@login_required
def comment_remove(request, id):
    try:
        comentario =comentarios.objects.get(id =id)
    except comentarios.DoesNotExist:
        raise Http404('Comentario no existe')
    noticia_id = comentario.noticia.id
    comentario.delete()
    return redirect('noticia_detalle', id=noticia_id)


@login_required
def agregar_comentario(request, id):
    datanoticia=noticia.objects.get( id=id)
    if request.method=='POST':
        form = CommentarioForm(request.POST)
        if form.is_valid():
            print("Validacion exitosa!")
            print("Autor:" + form.cleaned_data["autor"])
            print("Comentario:" + form.cleaned_data["cuerpo_comentarios"])
            comment = comentarios(
            autor=form.cleaned_data["autor"],
            cuerpo_comentarios=form.cleaned_data["cuerpo_comentarios"],
            noticia=datanoticia
            )
            comment.save()
            noticia_id= noticia.id
            return redirect("noticia_detalle",id=noticia_id)
    else:
        form= CommentarioForm()
    context={"form":form,}   

    return render(request,"noticiasdetalle.html",context)