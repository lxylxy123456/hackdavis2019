from django.conf.urls import *
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^login/$', views.login, name='index'),
]

