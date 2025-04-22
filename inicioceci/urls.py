from django.urls import path
from inicioceci.views import inicio, crear_especialidad, listado_de_especialidades, detalle_especialidad, VistaDetalleEspecialidad, VistaModificarEspecialidad, VistaEliminarEspecialidad

urlpatterns = [
    path('', inicio, name='inicio'),
    path('especialidad/crear/' , crear_especialidad, name='crear_especialidad'),
    path('especialidad/' , listado_de_especialidades, name='listado_de_especialidades'),
    path('especialidad/<int:pk>/' , VistaDetalleEspecialidad.as_view(), name='detalle_especialidad'),
    path('especialidad/<int:pk>/modificar/' , VistaModificarEspecialidad.as_view(), name='modificar_especialidad'),
    path('especialidad/<int:pk>/eliminar/' , VistaEliminarEspecialidad.as_view(), name='eliminar_especialidad'),
    #path('especialidad/<int:especialidad_en_especifico>/' , detalle_especialidad, name='detalle_especialidad'),
    #path('especialidad/<int:especialidad_en_especifico>/' , VistaDetalleEspecialidad.as_view(), name='detalle_especialidad'),
    #path('especialidad/detalles/' , name='detalle_especialidad'),
    #path('especialidad/eliminar/' , name='eliminar_especialidad'),
    #path('especialidad/modificar/' , name='modificar_especialidad'),
]