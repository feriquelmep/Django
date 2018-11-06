from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Persona, Mascota
from .forms import RegistrarPersonaForm, RegistrarMascotaForm

# Create your views here.
#Vista Index
def index(request):
    plantilla=loader.get_template("index.html")
    contexto={
        'titulo':"index",
    }
    return HttpResponse(plantilla.render(contexto, request))

#Vista Persona
def registroPersona(request):
    personas=Persona.objects.all()
    form=RegistrarPersonaForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        registroBD=Persona(rutPersona=data.get("rutPersona"), nombrePersona=data.get("nombrePersona"), emailPersona=data.get("emailPersona"), passwordPersona=data.get("passwordPersona"), viviendaPersona=data.get("viviendaPersona"))
        registroBD.save()
    form=RegistrarPersonaForm()
    return render(request,"registro.html",{'form':form,'personas':personas})


#Vista Mascota

def registroMascota(request):
    mascotas=Mascota.objects.all()
    form=RegistrarMascotaForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        registroBD=Persona(fotoMascota=data.get("fotoMascota"), nombreMascota=data.get("nombreMascota"), razaMascota=data.get("razaMascota"), descripcionMascota=data.get("descripcionMascota"), estadoMascota=data.get("estadoMascota"))
        registroBD.save()
    form=RegistrarMascotaForm()
    return render(request,"registroMascota.html",{'form':form,'mascostas':mascotas})