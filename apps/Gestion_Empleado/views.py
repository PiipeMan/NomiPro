from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.Gestion_Empleado.forms import CargoForm, TipoVinculacionForm, EmpleadosForm
from django.views.generic import CreateView, ListView, UpdateView
from apps.Gestion_Empleado.models import Cargo, TipoVinculacion, Empleado
from django.urls import reverse_lazy

#index 
def index(request):
   return render(request,"base/base.html")

## formularios Cargo

class CargoList(ListView):
   model=Cargo
   template_name='Gestion_Empleados/cargos_list.html'

class CargoCreate(CreateView):
   model=Cargo
   template_name='Gestion_Empleados/cargos_form.html'
   form_class=CargoForm
   success_url=reverse_lazy('cargos_listar')


class CargoUpdate(UpdateView):
   model=Cargo
   form_class=CargoForm
   template_name='Gestion_Empleados/cargos_form.html'   
   success_url=reverse_lazy('cargos_listar')

## formularios tipovinculacion
class TipoVinculacionList(ListView):
  model=TipoVinculacion
  template_name='Gestion_Empleados/tipo_vinculacion_list.html'
   
class TipoVinculacionCreate(CreateView):
   model=TipoVinculacion
   form_class=TipoVinculacionForm
   template_name='Gestion_Empleados/tipo_vinculacion_form.html'   
   success_url=reverse_lazy('tipovinculacion_listar')

class TipoVinculacionUpdate(UpdateView):
   model=TipoVinculacion
   form_class=TipoVinculacionForm
   template_name='Gestion_Empleados/tipo_vinculacion_form.html'   
   success_url=reverse_lazy('tipovinculacion_listar')  
   
## formularios empleado

class EmpleadoCreate(CreateView):
   model=Empleado
   form_class=EmpleadosForm
   template_name='Gestion_Empleados/empleado_form.html'   
   success_url=reverse_lazy('empleado_listar')

class EmpleadoList(ListView):
   model= Empleado
   template_name='Gestion_Empleados/empleado_list.html'
   
class EmpleadoUpdate(UpdateView):
   model=Empleado
   form_class=EmpleadosForm
   template_name='Gestion_Empleados/empleado_form.html'   
   success_url=reverse_lazy('empleado_listar')

# Create your views here.
