from django import forms

class FormularioEmpleado(forms.Form):
    
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    puesto = forms.CharField(max_length=50)
    

    

class FormularioVacante(forms.Form):
    
    titulo = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=300)
    requisitos = forms.CharField(max_length=300)
    salario = forms.IntegerField()
    


class FormularioDepartamento(forms.Form):
    
    nombre = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=300)
    
