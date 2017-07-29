from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import User


class UserCreate(CreateView):
    model = User
    template_name = 'accounts/form.html'
    fields = ("user_id", "user_name", "password" )
    success_url = reverse_lazy('accounts:form')
