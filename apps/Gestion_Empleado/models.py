from django.db import models

# Create your models here.
class Cargo(models.Model):
    ID_Cargo=models.AutoField(primary_key=True)
    Nombre=models.CharField(max_length=40)
    Estado=models.CharField(max_length=1)
    Valor_cargo=models.FloatField()


class TipoVinculacion(models.Model):
    ID_TipoVinculacion=models.AutoField(primary_key=True)
    Descripcion=models.CharField(max_length=40)
    Estado=models.CharField(max_length=1) 

class Empleado(models.Model):
    ID_Empleado=models.CharField(max_length=40, primary_key=True)
    Nombre=models.CharField(max_length=40)
    Apellido=models.CharField(max_length=40)
    Correo=models.EmailField(max_length=254)
    Telefono=models.IntegerField()
    Tipo_Documento=models.CharField(max_length=40)
    ID_Cargo=models.ForeignKey(Cargo,null=True, blank=True, on_delete=models.CASCADE)
    ID_TipoVinculacion=models.ForeignKey(TipoVinculacion,null=True, blank=True, on_delete=models.CASCADE)   