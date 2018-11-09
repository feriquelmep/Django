from . import views
from django.conf.urls import url
from django.urls import path

#Todos los urls para las páginas
urlpatterns=[
    url(r'^$', views.index, name="inicio"),
    url(r'^index/$', views.index, name="index"),
    url(r'^login/$', views.ingresar, name="login"),
    url(r'^registroPersona/$', views.registroPersona, name="RegistroPersona"),
    url(r'^registroMascota/$', views.registroMascota, name="RegistroMascota"),
    url(r'^logout/$', views.salir, name="logout"),
]