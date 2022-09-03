from django.shortcuts import render
from .models import Photo, Revistas

# Create your views here.
def galeria(request):
    photos = Photo.objects.all()
    revistas = Revistas.objects.all()

    context = {"photos": photos, "revistas": revistas}
    return render(request, 'galeria.html', context)


def viewPhoto(request,pk):
    
    return render(request, 'photo.html')