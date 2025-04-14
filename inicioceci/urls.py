from django.urls import path
from inicioceci.views import inicio, crear_especialidad, listado_de_especialidades

urlpatterns = [
    path('', inicio, name='inicio'),
    path('especialidad/crear/' , crear_especialidad, name='crear_especialidad'),
    path('especialidad/' , listado_de_especialidades, name='listado_de_especialidades'),
]