"""proyectofontana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import  include,path
from django.urls import re_path as url
from django.conf.urls.static import static
from django.conf import settings
from apps.noticias_app import views
from apps.eventos_app.views import eventos




urlpatterns =[
    path('admin/', admin.site.urls),

    path('', views.inicio, name='inicio'),
    
    path('login/', include('apps.login_app.urls'), name='login'),
    
    path('nosotros', views.nosotros, name='nosotros'),

    url('noticias/', include('apps.noticias_app.urls')),

    path('noticias', views.noticias, name='noticias'),

    path('registration', include('apps.login_app.urls')),

    path('eventos', eventos, name='eventos'),
    
    
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT,show_indexes=True)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT,show_indexes=True)

