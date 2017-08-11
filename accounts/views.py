from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from .forms import UserForm
from django import forms
from .models import User


class UserCreate(CreateView):
    form_class = UserForm
    template_name = 'accounts/form.html'
    success_url = reverse_lazy('accounts:form')
