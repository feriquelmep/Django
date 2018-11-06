from . import views
from django.conf.urls import url

urlpatterns=[
    url(r'^$', views.index, name="inicio"),
    url(r'^index/$', views.index, name="inicio"),
    url(r'^registroPersona/$', views.registroPersona, name="RegistroPersona"),
     url(r'^registroMascota/$', views.registroMascota, name="RegistroMascota"),
]