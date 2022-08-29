from django import forms
from django.forms import widgets
from .models import noticia, comentarios

class NoticiaForm(forms.ModelForm):

    class Meta:
        model = noticia
        fields = ('autor', 'titulo', 'contenido', 'categorias')

        widgets ={
            'titulo': forms.TextInput(attrs={'class':'textIntputClass'}),
            'contenido': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }

class CommentarioForm(forms.Form):
        model = comentarios
        fields = ('autor', 'cuerpo_comentario',)

        autor = forms.CharField(
            max_length=60,
            widget=forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ingresa tu nombre"
            })
        )
        cuerpo_comentario = forms.CharField(widget=forms.Textarea(
            attrs={
                "class": "form-control comment-textarea",
                "id":"comment",
                "placeholder": "Dinos que piensas, dejanos un comentario!"
            })
        )