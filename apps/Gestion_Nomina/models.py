from django.db import models
from apps.Gestion_Empleado.models import Empleado

# Create your models here.
class Periodo(models.Model):
    ID_Periodo=models.AutoField(primary_key=True)
    Anual=models.CharField(max_length=40)
    Mes=models.CharField(max_length=40)

class Nomina(models.Model):
    ID_Nomina=models.AutoField(primary_key=True)
    ID_Empleado=models.ForeignKey(Empleado, null=True, blank=True, on_delete=models.CASCADE) 
    ID_Periodo=models.ForeignKey(Periodo, null=True, blank=True, on_delete=models.CASCADE)    
    Estado=models.CharField(max_length=1)
    Valor_Pagar=models.FloatField(null=True, blank=True)
    Subtotal=models.FloatField(null=True, blank=True)
    Total= models.FloatField(null=True, blank=True)
    
    
    