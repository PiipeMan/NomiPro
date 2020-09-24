from django.db import models
from apps.Gestion_Empleado.models import Empleado, Cargo, TipoVinculacion
from apps.Gestion_Nomina.models import Nomina, Periodo
# Create your models here.
class ReporteHoras(models.Model):
    ID_ReporteHoras=models.AutoField(primary_key=True)
    ID_Empleado=models.ForeignKey(Empleado, null=True, blank=True, on_delete=models.CASCADE)
    ID_Periodo=models.ForeignKey(Periodo, null=True, blank=True, on_delete=models.CASCADE)
    Numero_Horas=models.IntegerField()

class HorasAdicionales(models.Model):
    ID_HorasAdicionales=models.AutoField(primary_key=True)
    Nombre=models.CharField(max_length=40)
    Valor=models.FloatField()
    Estado=models.CharField(max_length=1)
    

class Parafiscales(models.Model):
    ID_PArafiscales=models.AutoField(primary_key=True)
    Nombre=models.CharField(max_length=40)
    Valor=models.FloatField()
    Estado=models.CharField(max_length=1)
    Id_TipoVinculacion=models.ForeignKey(TipoVinculacion,null=True, blank=True, on_delete=models.CASCADE)

class DetalleParafiscales(models.Model):
    ID_DetalleParafiscal=models.AutoField(primary_key=True)
    ID_Nomina=models.ForeignKey(Nomina, null=True, blank=True, on_delete=models.CASCADE)
    Total_Parafiscales=models.FloatField()
    ID_Parafiscales=models.ForeignKey(Parafiscales, null=True, blank=True, on_delete=models.CASCADE)

class DetalleHoras(models.Model):
    ID_DetalleHoras=models.AutoField(primary_key=True)
    ID_Nomina=models.ForeignKey(Nomina, null=True, blank=True, on_delete=models.CASCADE)
    ID_HorasAdicionales=models.ForeignKey(HorasAdicionales, null=True, blank=True, on_delete=models.CASCADE)
    Total=models.FloatField()
    Cantidad=models.IntegerField()
