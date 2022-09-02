from pyexpat import model
from django import forms
from .models import comentarios

class FormComment(forms.Form):
	model = comentarios
	fields = ('cuerpo_comentario')

	cuerpo_comentario = forms.CharField(widget=forms.Textarea)