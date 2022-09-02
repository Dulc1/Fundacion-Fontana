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
from apps.noticias_app import views as  viewsNotice
from apps.eventos_app.views import eventos
from apps.eventos_app import views as viewsEvents
from django.conf.urls.static import static
from django.conf import settings




urlpatterns =[
    path('admin/', admin.site.urls),

    path('', viewsNotice.inicio, name='inicio'),
    
    path('login/', include('apps.login_app.urls'), name='login'),
    
    path('nosotros', viewsNotice.nosotros, name='nosotros'),

    url('noticias/<int:id>', viewsNotice.noticiaDetalle, name='Noticia' ),

    path('noticias', viewsNotice.noticias, name='noticias'),

    path('comentarios/<int:id>', viewsNotice.commentAproved, name='comentAproved'),
    
    path('categoria/<int:id>', viewsNotice.categoriaDetail, name='Noticia'),

    path('registration', include('apps.login_app.urls')),

    path('eventos', eventos, name='eventos'),

    path('eventos', viewsEvents.eventos, name='eventos'),


    path('evento/<int:id>', viewsEvents.eventDetail, name='eventDetail'),
    
    
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT,show_indexes=True)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT,show_indexes=True)

