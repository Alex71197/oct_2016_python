from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^getgold$', views.getgold),
    url(r'^reset$', views.reset)
]
