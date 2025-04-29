from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicioceci.forms import CreacionEspecialidad
from inicioceci.models import Especialidad
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def inicio(request):
    #return HttpResponse('HolaCeci')
    return render(request, 'inicioceci/inicio.html')

@login_required
def crear_especialidad(request):

    formulario = CreacionEspecialidad()

    print('ESTOS SON LOS DATOS DEL GET -->', request.GET)
    print('ESTOS SON LOS DATOS DEL POST -->', request.POST)
    
    if request.method == "POST":
        formulario = CreacionEspecialidad(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            especialidad = Especialidad(nombre=info.get('nombre'), tipo=info.get('tipo'), fecha_creation=info.get('fecha_creation'))
            especialidad.save()
            return redirect('inicio')
        else:
            formulario = CreacionEspecialidad()
    
    return render(request, 'inicioceci/crear_especialidad.html', {'formulario': formulario})

def listado_de_especialidades(request):
    especialidades = Especialidad.objects.all()
    return render(request, 'inicioceci/listado_de_especialidades.html',{'especialidades': especialidades})

#vista normal

def detalle_especialidad(request, especialidad_en_especifico):
    especialidad = Especialidad.objects.get(id=especialidad_en_especifico)
    return render(request, 'inicioceci/detalle_especialidad.html', {'especialidad': especialidad})

#clase basada en vista
class VistaDetalleEspecialidad(DetailView):
    model = Especialidad
    template_name = "inicioceci/detalle_especialidad.html"

#clase basada en vista de edicion
class VistaModificarEspecialidad(LoginRequiredMixin, UpdateView):
    model = Especialidad
    template_name = "inicioceci/modificar_especialidad.html"
    fields = ["nombre", "tipo", "fecha_creation"]
    succes_url = reverse_lazy('listado_de_especialidades')

#clase para eliminar
class VistaEliminarEspecialidad(LoginRequiredMixin, DeleteView):
    model = Especialidad
    template_name = "inicioceci/eliminar_especialidad.html"
    success_url = reverse_lazy('listado_de_especialidades')