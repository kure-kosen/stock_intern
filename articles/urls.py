from django.conf.urls import url
from articles.views import IndexView
from . import views

app_name = 'articles'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
]

