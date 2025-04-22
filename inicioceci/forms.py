from django import forms

class CreacionEspecialidad(forms.Form):
    nombre = forms.CharField(max_length=20)
    tipo = forms.CharField(max_length=20)
    #fecha_creation = forms.DateField()
    fecha_creation = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    