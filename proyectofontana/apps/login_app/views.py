
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm

# Create your views here.
class Login(auth_views.LoginView):
    """vista de login usuario"""
    template_name = 'login/login.html'


class logout(LoginRequiredMixin, auth_views.LogoutView):
    """vista de logout usuario"""
    template_name = 'registration/logged_out.html'

class SignUpView(FormView):
    """vista de signup usuario"""
    template_name = 'registration/registro.html'
    form_class=SignUpForm
    success_url: reverse_lazy('apps.login_app:registrocomplete')

    def form_valid(self, form):
        """verificamos que los datos sean validos"""
        form.save()
        return super().form_valid(form)

    class WelcomeView(CreateView):
        template_name = 'welcome.html'












