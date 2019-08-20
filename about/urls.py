from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^logout/$', views.logoutView, name="logout"),
    url(r'^login/$', views.loginView, name="login"),
    url(r'^$', views.index, name="index"),
    url(r'^data/$', views.data),
    url(r'^nilai/$', views.nilai),
    url(r'^spp/$', views.spp),
    url(r'^semua/$', views.semua, name="semua"),
    url(r'^$', views.index),
]