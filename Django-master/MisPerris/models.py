from django.db import models
from django.contrib.auth.models import User


# Create your models here.cd
#Tabla de la Persona
#La clase Usuario, por defecto, guarda username, password and email
class Persona(models.Model):
    usuario=models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    nombrePersona=models.CharField(max_length=20)
    apellidoPersona=models.CharField(max_length=20)
    viviendaPersona=models.CharField(max_length=40)

#Tabla de la Mascota
class Mascota(models.Model):
    fotoMascota=models.ImageField()
    nombreMascota=models.CharField(max_length=20)
    razaMascota=models.CharField(max_length=20)
    descripcionMascota=models.CharField(max_length=20)
    estadoMascota=models.CharField(max_length=20)




