from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^recent/$', views.recent),
    url(r'^news/$', views.news),
    url(r'^$', views.index),
]