from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1: forms.CharField(max_length=70, widget=forms.PasswordInput())
    password2: forms.CharField(max_length=70, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields =(
            'username',
            'email',
            'password1',
            'password2'
        )

    def clean(self):
        """Verifico que las contraseñas sean iguales """
        data = super().clean()
        password1=data['password1']
        password2=data['password2']

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")

        return data
    