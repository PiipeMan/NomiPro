from django import forms
from apps.Gestion_Tiempo.models import ReporteHoras, HorasAdicionales, Parafiscales, DetalleParafiscales, DetalleHoras

class ReporteHorasForm(forms.ModelForm):
    class Meta:
        model= ReporteHoras
        fields = [
            'ID_ReporteHoras',
            'ID_Empleado',
            'ID_Periodo',
            'Numero_Horas',
        ]
        labels = {
            'ID_ReporteHoras':'ID Reporte Horas:',
            'ID_Empleado': 'ID Empleado:',
            'ID_Periodo': 'ID Periodo:',
            'Numero_Horas': 'Número de horas a reportar:',

        }
        widgets = {
            'ID_ReporteHoras': forms.TextInput(attrs={'class':'form-control'}),
            'ID_Empleado': forms.TextInput(attrs={'class':'form-control'}),
            'ID_Periodo': forms.TextInput(attrs={'class':'form-control'}),
            'Numero_Horas': forms.TextInput(attrs={'class':'form-control'}),
            
        }

    

class HorasAdicionalesForm(forms.ModelForm):
    class Meta:
        model= HorasAdicionales
        fields = [
            'ID_HorasAdicionales',
            'Nombre',
            'Valor',
            'Estado',
            
        ]
        labels = {
            'ID_HorasAdicionales': 'ID horas adicionales:',
            'Nombre': 'Descripción hora adicional:',
            'Valor': 'Valor asignado hora adicional:',
            'Estado': 'Estado:',
            

        }
        widgets = {
            'ID_HorasAdicionales': forms.TextInput(attrs={'class':'form-control'}),
            'Nombre': forms.TextInput(attrs={'class':'form-control'}),
            'Valor': forms.TextInput(attrs={'class':'form-control'}),
            'Estado': forms.TextInput(attrs={'class':'form-control'}),
            
            
        }
    

class ParafiscalesForm(forms.ModelForm):
    class Meta:
        model= Parafiscales
        fields = [
            'ID_PArafiscales',
            'Nombre',
            'Valor',
            'Estado',
            'Id_TipoVinculacion'
        ]
        labels = {
            'ID_PArafiscales': 'ID Parafiscales:',
            'Nombre': 'Nombre parafiscal:',
            'Valor': 'Valor',
            'Estado': 'Estado:',
            'Id_TipoVinculacion': 'ID Tipo vinculación:',

        }
        widgets = {
            'ID_PArafiscales': forms.TextInput(attrs={'class':'form-control'}),
            'Nombre': forms.TextInput(attrs={'class':'form-control'}),
            'Valor': forms.TextInput(attrs={'class':'form-control'}),
            'Estado': forms.TextInput(attrs={'class':'form-control'}),
            'Id_TipoVinculacion': forms.TextInput(attrs={'class':'form-control'}),
            
        }
    
class DetalleParafiscalesForm(forms.ModelForm):
    class Meta:
        model= DetalleParafiscales
        fields = [
            'ID_DetalleParafiscal',
            'ID_Nomina',
            'Total_Parafiscales',
            'ID_Parafiscales',
        ]
        labels = {
            'ID_DetalleParafiscal': 'ID Detalle parafiscal:',
            'ID_Nomina': 'ID Nómina:',
            'Total_Parafiscales': 'Total parafiscales:',
            'ID_Parafiscales': 'ID Parafiscales:',

        }
        widgets = {
            'ID_DetalleParafiscal': forms.TextInput(attrs={'class':'form-control'}),
            'ID_Nomina': forms.TextInput(attrs={'class':'form-control'}),
            'Total_Parafiscales': forms.TextInput(attrs={'class':'form-control'}),
            'ID_Parafiscales': forms.TextInput(attrs={'class':'form-control'}),

        }
    

class DetalleHorasForm(forms.ModelForm):
    class Meta: 
        model= DetalleHoras
        fields = [
            'ID_DetalleHoras',
            'ID_Nomina',
            'ID_HorasAdicionales',
            'Total',
            'Cantidad',
        ]
        labels = {
            'ID_DetalleHoras': 'ID Detalle horas:',
            'ID_Nomina': 'ID Nómina:',
            'ID_HorasAdicionales': 'ID Horas adicionales:',
            'Total': 'Total:',
            'Cantidad': 'Cantidad:',

        }
        widgets = {
            'ID_DetalleHoras': forms.TextInput(attrs={'class':'form-control'}),
            'ID_Nomina': forms.TextInput(attrs={'class':'form-control'}),
            'ID_HorasAdicionales': forms.TextInput(attrs={'class':'form-control'}),
            'Total': forms.TextInput(attrs={'class':'form-control'}),
            'Cantidad': forms.TextInput(attrs={'class':'form-control'}),
            
        }
    