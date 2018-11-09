from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
#Librerias para validar
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
#Libreria importacion de modelos y formulario
from .models import Persona, Mascota
from .forms import RegistrarPersonaForm, RegistrarMascotaForm, LoginForm

# Create your views here.
#Vista Index
def index(request):
    plantilla=loader.get_template("index.html")
    contexto={
        'titulo':"index",
    }
    return HttpResponse(plantilla.render(contexto, request))

#Vista registro persona
def registroPersona(request):
    personas=Persona.objects.all()
    form=RegistrarPersonaForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        new=User.objects.create_user(data.get("rutPersona"),data.get("emailPersona"),data.get("passwordPersona"))
        new.is_staff=False
        new.save()
        regDB=Persona(usuario=new,nombrePersona=data.get("nombrePersona"),apellidoPersona=data.get("apellidoPersona"), viviendaPersona=data.get("viviendaPersona"))
        regDB.save()
    form=RegistrarPersonaForm()
    return render(request,"registro.html",{'form':form,'personas':personas,})

#Vista Login
def ingresar(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("username"), password=data.get("password"))
        if user is not None:
            login(request,user)
            return redirect('/index/')
    return render(request,"login.html",{'form':form})


#Vista Logout
def salir(request):
    logout(request)
    return redirect('/index/')


#Vista Mascota
#Registrar Mascota
def registroMascota(request):
    mascotas=Mascota.objects.all()
    form=RegistrarMascotaForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        registroDB=Persona(fotoMascota=data.get("fotoMascota"), nombreMascota=data.get("nombreMascota"), razaMascota=data.get("razaMascota"), descripcionMascota=data.get("descripcionMascota"), estadoMascota=data.get("estadoMascota"))
        registroDB.save()
    form=RegistrarMascotaForm()
    return render(request,"registroMascota.html",{'form':form,})

#Listar Mascota
#Modificar Mascota
#Eliminar Mascota
