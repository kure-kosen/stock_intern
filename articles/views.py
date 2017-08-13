from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView
from django.core.urlresolvers import reverse_lazy
from .models import Article

class IndexView(ListView):
    model = Article
    template_name = 'articles/index.html'
    context_object_name = 'articles'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context["foo"] = 'bar'
        return context
    

class ArticleCreate(CreateView):
    model = Article
    template_name = 'accounts/form.html'
    fields = ("title", "text", "user_id", "category_id")
    success_url = reverse_lazy('articles:form')
