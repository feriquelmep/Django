from . import views
from django.conf.urls import url, include
from rest_framework import routers

#Todos los urls para las páginas

router = routers.DefaultRouter()
router.register(r'persona', views.PersonaViewSet)

urlpatterns=[
    url(r'^$', views.index, name="inicio"),
    url(r'^index/$', views.index, name="index"),
    url(r'^login/$', views.login, name="login"),
    url(r'^registroPersona/$', views.registroPersona, name="RegistroPersona"),
    url(r'^registroMascota/$', views.registroMascota, name="RegistroMascota"),
    url(r'^', include(router.urls)),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework')),
]