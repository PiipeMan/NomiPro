from django import forms
from apps.Gestion_Empleado.models import Empleado, TipoVinculacion, Cargo

class EmpleadosForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'ID_Empleado',
            'Nombre',
            'Apellido',
            'Correo',
            'Telefono',
            'Tipo_Documento',
        ]
        labels ={
            'ID_Empleado': 'Documento de identidad:',
            'Tipo_Documento': 'Tipo de documento',
            'Nombre': 'Nombre:',
            'Apellido': 'Apellidos:',
            'Correo': 'E-mail:',
            'Telefono': 'Número de contacto',            
        }
        widgets = {
            'ID_Empleado': forms.TextInput(attrs={'class':'form-control'}),
            'Tipo_Documento':forms.TextInput(attrs={'class':'form-control'}),
            'Nombre': forms.TextInput(attrs={'class':'form-control'}),
            'Apellido': forms.TextInput(attrs={'class':'form-control'}),
            'Correo': forms.TextInput(attrs={'class':'form-control'}),
            'Telefono': forms.TextInput(attrs={'class':'form-control'}),
        }

class TipoVinculacionForm(forms.ModelForm):
    class Meta:
        model = TipoVinculacion
        fields = [
            'ID_TipoVinculacion',
            'Descripcion',
            'Estado',
        ]
        labels = {
            'ID_TipoVinculacion':'ID tipo de vinculación:',
            'Descripcion':'Tipo de contrato:',
            'Estado':'Estado:',
        }
        widgets = {
            'ID_TipoVinculacion': forms.TextInput(attrs={'class':'form-control'}),
            'Descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'Estado': forms.TextInput(attrs={'class':'form-control'}),
        }

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = [
            'ID_Cargo',
            'Nombre',
            'Estado',
            'Valor_cargo',
        ]
        labels = {
            'ID_Cargo':'ID cargo::',
            'Nombre':'Nombre del cargo:',
            'Estado':'Estado:',
            'Valor_cargo': 'Valor asignado al cargo:',
        }
        widgets = {
            'ID_Cargo': forms.TextInput(attrs={'class':'form-control'}),
            'Nombre': forms.TextInput(attrs={'class':'form-control'}),
            'Estado': forms.TextInput(attrs={'class':'form-control'}),
            'Valor_cargo': forms.TextInput(attrs={'class':'form-control'}),
        }

