from django.conf.urls import url
from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^form$', views.form_test),
]

