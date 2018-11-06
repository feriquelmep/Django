from django.db import models

# Create your models here.
#Tabla Persona
class Persona(models.Model):
    rutPersona=models.CharField(max_length=10,primary_key=True)
    passwordPersona=models.CharField(max_length=10)
    nombrePersona=models.CharField(max_length=10)
    emailPersona=models.CharField(max_length=10)
    viviendaPersona=models.CharField(max_length=40)

#Tabla Mascota
class Mascota(models.Model):
    fotoMascota=models.ImageField()
    nombreMascota=models.CharField(max_length=20)
    razaMascota=models.CharField(max_length=20)
    descripcionMascota=models.CharField(max_length=20)
    estadoMascota=models.CharField(max_length=20)




