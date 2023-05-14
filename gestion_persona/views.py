from django.shortcuts import get_object_or_404, render
from gestion_persona.models import Persona
from django.views import View 
from gestion_persona.forms import Buscar, PersonaForm


def bienvenida(request):
    return render(request, 'bienvenida.html')

def MostrarHuesped(request):
    lista_huesped = Persona.objects.all()
    return render(request, 'huespedes.html', {'lista_huesped':lista_huesped})
  
  
class BuscarHuesped(View):
    form_class = Buscar
    template_name = 'buscarHuesped.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_persona = Persona.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_persona':lista_persona})
        return render(request, self.template_name, {"form": form})

class AltaHuesped(View):

    form_class = PersonaForm
    template_name = 'altaHuesped.html'
    initial = {"dni":"", "nombre":"", "apellido":"", "fecha_entrada":"", "telefono":"", "email":"", "direccion":"", "habitacion_nro":"", "habitacion_disponible":"", "fecha_salida":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"SE CARGO CON EXITO"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class ActualizarHuesped(View):
  form_class = PersonaForm
  template_name = 'actualizarHuesped.html'
  initial = {"dni":"", "nombre":"", "apellido":"", "fecha_entrada":"", "telefono":"", "email":"", "direccion":"", "habitacion_nro":"", "habitacion_disponible":"", "fecha_salida":""}

  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, dni): 
      persona = get_object_or_404(Persona, dni=dni)
      form = self.form_class(instance=persona)
      return render(request, self.template_name, {'form':form,'persona': persona})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, dni): 
      persona = get_object_or_404(Persona, dni=dni)
      form = self.form_class(request.POST ,instance=persona)
      if form.is_valid():
          form.save()
          msg_exito = f"SE ACTUALIZACÓ CON EXITO"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'persona': persona,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class BorrarHuesped(View):
  template_name = 'gestion_persona/huespedes.html'

  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, dni): 
      persona = get_object_or_404(Persona, dni=dni)
      persona.delete()
      persona = Persona.objects.all()
      return render(request, self.template_name, {'lista_persona': persona})