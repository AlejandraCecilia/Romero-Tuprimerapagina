from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicioceci.forms import CreacionEspecialidad
from inicioceci.models import Especialidad

def inicio(request):
    #return HttpResponse('HolaCeci')
    return render(request, 'inicioceci/inicio.html')

def crear_especialidad(request):

    formulario = CreacionEspecialidad()

    print('ESTOS SON LOS DATOS DEL GET -->', request.GET)
    print('ESTOS SON LOS DATOS DEL POST -->', request.POST)
    
    if request.method == "POST":
        formulario = CreacionEspecialidad(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            especialidad = Especialidad(nombre=info.get('nombre'), tipo=info.get('tipo'))
            especialidad.save()
            return redirect('inicio')
        else:
            formulario = CreacionEspecialidad()
    
    return render(request, 'inicioceci/crear_especialidad.html', {'formulario': formulario})

def listado_de_especialidades(request):
    especialidades = Especialidad.objects.all()
    return render(request, 'inicioceci/listado_de_especialidades.html',{'especialidades': especialidades})
# Create your views here.
