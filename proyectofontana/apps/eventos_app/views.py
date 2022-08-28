
# Create your views here.from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def eventos(request):
    
    return render (request, "eventos.html")

