from django.conf.urls import url
from . import views

app_name = 'articles'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^form/$', views.ArticleCreate.as_view(), name='form'),
    url(r'^home/$', views.home, name='home'),
]

