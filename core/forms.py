from multiprocessing import managers
from django import forms

#API FORMS EXAMPLE
class FormularioContacto(forms.Form):
    asunto=forms.CharField()
    email=forms.EmailField()
    mensaje=forms.CharField()
