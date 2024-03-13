from django.shortcuts import render
from AppWeb.models import *
from AppWeb.forms import *
# Create your views here.

def inicio(request):
    
    return render(request, 'AppWeb/inicio.html')

def confirmacion_guardar(request):
    
   return render(request, 'AppWeb/confirmacion_guardar.html')

def vacante_nueva(request):

    if request.method == "POST":

        formulario = FormularioVacante(request.POST) #almacena la informacion que se ha puesto en el form

        if formulario.is_valid():

            info_dic = formulario.cleaned_data #convierte la info del form a un diccionario de python

            vacante_nueva = Vacante(
                titulo=info_dic["titulo"],
                descripcion=info_dic["descripcion"],
                requisitos=info_dic["requisitos"],
                salario=info_dic["salario"],
                
                )
            
            vacante_nueva.save()
            
            return render(request, "AppWeb/confirmacion_guardar.html")
        
    else:
            
        formulario = FormularioVacante()
    
    
    
    return render(request, 'AppWeb/vacante_nueva.html', {'formu': formulario})



def depto_nuevo(request):
    
    if request.method == "POST":

        formulario = FormularioDepartamento(request.POST) #almacena la informacion que se ha puesto en el form

        if formulario.is_valid():

            info_dic = formulario.cleaned_data #convierte la info del form a un diccionario de python

            depto_nuevo = Departamento(
                nombre=info_dic["nombre"],
                descripcion=info_dic["descripcion"],
                
                
                )
            
            depto_nuevo.save()
            
            return render(request, "AppWeb/confirmacion_guardar.html")
        
    else:
            
        formulario = FormularioDepartamento()
    
    
    
    return render(request, 'AppWeb/depto_nuevo.html', {'formu':formulario})
    
    

def empleado_nuevo(request):
    
    if request.method == "POST":

        formulario = FormularioEmpleado(request.POST) #almacena la informacion que se ha puesto en el form

        if formulario.is_valid():

            info_dic = formulario.cleaned_data #convierte la info del form a un diccionario de python

            empleado_nuevo = Empleado(
                nombre=info_dic["nombre"],
                apellido=info_dic["apellido"],
                puesto=info_dic["puesto"],
                
                )
            
            empleado_nuevo.save()
            
            return render(request, "AppWeb/confirmacion_guardar.html")
        
    else:
            
        formulario = FormularioEmpleado()
    
    
    
    return render(request, 'AppWeb/empleado_nuevo.html', {'formu': formulario})



def buscar_empleado(request):
    
    return render(request, "AppWeb/buscar_empleado.html")


def resultado_empleado(request):
    
    empleado = request.GET["empleado"]
    
    resultados = Empleado.objects.filter(nombre__iexact=empleado)
    
    return render(request, 'AppWeb/resultado_empleado.html', {'resultados':resultados})