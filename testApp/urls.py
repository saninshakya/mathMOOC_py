from django.conf.urls import patterns, url

from testApp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
