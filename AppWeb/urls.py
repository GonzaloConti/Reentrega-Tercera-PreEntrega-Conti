from django.urls import path
from AppWeb.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    
    path('ConfirmacionDeInformacionGuardada/', confirmacion_guardar),
    
    path('empleado_nuevo/', empleado_nuevo, name= 'empleado_nuevo'),
    path('depto_nuevo/', depto_nuevo, name= 'depto_nuevo'),
    path('vacante_nueva/', vacante_nueva, name= 'vacante_nueva'),
    
    path('buscar_empleado/', buscar_empleado, name='buscar_empleado'),
    
    path('resultados/', resultado_empleado),
]