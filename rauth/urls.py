__author__ = 'nicc777'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.do_auth, name='index'),
]

