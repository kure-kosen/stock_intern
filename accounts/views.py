from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy
from .forms import UserForm
from django import forms
from .models import User


class IndexView(ListView):
    model = User
    template_name = 'accounts/index.html'
    context_object_name = 'users'


class UserCreate(CreateView):
    form_class = UserForm
    template_name = 'accounts/form.html'
    success_url = reverse_lazy('accounts:form')
