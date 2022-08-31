from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileUsers(admin.ModelAdmin):
    list_display= ('usuario', 'resume')