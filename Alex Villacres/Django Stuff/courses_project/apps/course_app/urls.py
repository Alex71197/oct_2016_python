from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^(?P<id>\d+)/destroy$', views.destroy),
    url(r'^confirm_destroy/(?P<id>\d+)$', views.confirm_destroy),
    ]
