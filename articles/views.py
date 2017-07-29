from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from .models import Article

class IndexView(TemplateView):
    template_name = 'articles/index.html'

class ArticleCreate(CreateView):
    model = Article
    template_name = 'accounts/form.html'
    fields = ("title", "text", "user_id", "category_id")
    success_url = reverse_lazy('articles:form')
