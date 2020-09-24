from django import forms
from apps.Gestion_Nomina.models import Nomina, Periodo

class PeriodoForm(forms.ModelForm):
    class Meta:
        model= Periodo

        fields = [
            'ID_Periodo',
            'Anual',
            'Mes',
            
        ]
        labels = {
            'ID_Periodo': 'ID del periodo:',
            'Anual': 'Año a pagar:',
            'Mes': 'Mes a pagar:',
        }
        widgets = {
            'ID_Periodo':forms.TextInput(attrs={'class':'form-control'}),
            'Anual':forms.TextInput(attrs={'class':'form-control'}),
            'Mes':forms.TextInput(attrs={'class':'form-control'}),
        }

class NominaForm(forms.ModelForm):
    class Meta:
        model= Nomina

        fields = [
            'ID_Nomina',
            'Valor_Pagar',
            'Subtotal',
            'ID_Periodo',
            'ID_Empleado',
            'Estado',
            'Total',
        ]
        labels = {
            'ID_Nomina': 'ID nómina:',
            'Valor_Pagar': 'Valor a pagar:',
            'Subtotal': 'Subtotal:',
            'ID_Periodo':'ID periodo:',
            'ID_Empleado': 'ID Empleado:',
            'Estado': 'Estado:',
            'Total': 'Total:',
        }
        widgets = {
            'ID_Nomina': forms.TextInput(attrs={'class':'form-control'}),
            'Valor_Pagar': forms.TextInput(attrs={'class':'form-control'}),
            'Subtotal': forms.TextInput(attrs={'class':'form-control'}),
            'ID_Periodo': forms.TextInput(attrs={'class':'form-control'}),
            'ID_Empleado': forms.TextInput(attrs={'class':'form-control'}),
            'Estado': forms.TextInput(attrs={'class':'form-control'}),
            'Total': forms.TextInput(attrs={'class':'form-control'}),
        }

