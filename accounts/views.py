from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.urls import path
from django.contrib import admin
# Create your views here.
class SingUp(CreateView):
    path('admin', admin.site.urls)
    template_name = "registration/singup.html"
    form_class = UserCreationForm
    url_success_url= reverse_lazy ('login')
    