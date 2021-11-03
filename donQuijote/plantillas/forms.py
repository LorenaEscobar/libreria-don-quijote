from django import forms

class FormularioContacto(forms.Form):
    asunto=forms.CharField(label="Asunto", required=True, max_length=100)
    nombre=forms.CharField(label="Nombre", required=True, max_length=100)
    email=forms.EmailField(label="Email", required=True)
    mensaje=forms.CharField(label="Mensaje", required=True, max_length=600)

