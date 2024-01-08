from django import forms

from .models import Login
from .models import Patient, File


class LogForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__"
        labels = {
            "user_name": "Nombre Administrador",
            "password": "Contraseña"
        }

        error_messages = {
            "user_name":{
                "required": "Usuario invalido"
            },
            "password":{
                "required": "Contraseña invalida"
            }
        }

      
class FileForm(forms.ModelForm):

    class Meta:
        model = File
        # fields = "__all__"
        exclude = ("patient", "date")
        labels = {
            "user_file": "Nombre de Archivo",
            "date": "Fecha"
        }

     
        # widgets = {'user_file':forms.HiddenInput()}


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        # fields = "__all__"
        exclude = ("slug",)
        labels = {
            "full_name": "Nombre Completo",
            "age": "Edad",
            "address": "Direccion",
            "p_number": "Telefono",
            "s_number": "Opcional"
        }

        error_messages  = {
            "full_name":{
                "required": "Nombre completo no debe estar en blanco",
                "max_length": "Porfavor ingresar un nombre corto"
            },
            "address": {
                "required":"Direccion no debe estar en blanco"
            },
            "age":{
                "required": "Edad no debe estar en blanco"
            }
        }
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['file'].required = False
    #     self.fields['file'].empty_label = "Select"

        
# class PatientForm(forms.Form):
#     user_name = forms.CharField(label="Patient Name", required=True, max_length=50)
#     last_name = forms.CharField(label="Patient Last Name", required=True, max_length=100)
#     file = forms.FileField(required=False)
#     slug = forms.SlugField(required=False)

# class PatientFilter(forms.Form):
#     full_name = forms.CharField()
