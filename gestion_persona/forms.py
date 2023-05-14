from django import forms
from gestion_persona.models import Persona


class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'Buscar huésped...'})) #queda un mensaje clarito en el box

class PersonaForm(forms.ModelForm):
  class Meta:
    model = Persona
    fields = ['dni', 'nombre', 'apellido', 'fecha_entrada','telefono','email','direccion','habitacion_nro','fecha_salida']