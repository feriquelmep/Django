from django import forms

class RegistrarPersonaForm(forms.Form):
    rutPersona=forms.CharField(widget=forms.TextInput(),label="Rut")
    passwordPersona=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
    nombrePersona=forms.CharField(widget=forms.TextInput(),label="Nombre")
    emailPersona=forms.EmailField(label="Email")
    viviendaPersona=forms.ChoiceField(choices=(('1', 'Casa con Patio Grande'),('2', 'Casa con Patio Pequeño'),('3', 'Casa sin Patio'),('4', 'Departamento')),label="Tipo Vivienda")
    #Lo de arriba, para la wea de ciudad y regiones de tshile

class RegistrarMascotaForm(forms.Form):
    fotoMascota=forms.ImageField(label="Imagen")
    nombreMascota=forms.CharField(widget=forms.TextInput(),label="Nombre")
    razaMascota=forms.CharField(widget=forms.TextInput(),label="Raza")
    descripcionMascota=forms.CharField(widget=forms.TextInput(),label="Descripcion")
    estadoMascota=forms.ChoiceField(choices=(('1', 'Rescatado'),('2', 'Disponible'),('3', 'Adoptado')),label="Estado")