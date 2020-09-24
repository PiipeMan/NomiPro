from django.conf.urls import url, include
from apps.Gestion_Empleado.views import index, CargoCreate,  CargoList, CargoUpdate
from apps.Gestion_Empleado.views import EmpleadoCreate, EmpleadoList, EmpleadoUpdate
from apps.Gestion_Empleado.views import TipoVinculacionCreate, TipoVinculacionUpdate, TipoVinculacionList
from django.contrib.auth.decorators import login_required

urlpatterns = [
     url(r'^$', index, name='Emp_index'),   
     url(r'^cargo/nuevo/$', login_required(CargoCreate.as_view()), name='cargos_crear'),
     url(r'^cargo/ver/', login_required(CargoList.as_view()), name='cargos_listar'),
     url(r'^cargo/editar/(?P<pk>\d+)/$', login_required(CargoUpdate.as_view()), name='cargos_editar'),     
     url(r'^tipovinculacion/nuevo/$', login_required(TipoVinculacionCreate.as_view()), name='tipovinculacion_crear'),
     url(r'^tipovinculacion/ver/', login_required(TipoVinculacionList.as_view()), name='tipovinculacion_listar'),
     url(r'^tipovinculacion/editar/(?P<pk>\d+)/$',login_required(TipoVinculacionUpdate.as_view()), name='tipovinculacion_editar'),     
     url(r'^empleado/nuevo/$', login_required(EmpleadoCreate.as_view()), name='empleado_crear'),
     url(r'^empleado/ver/', login_required(EmpleadoList.as_view()), name='empleado_listar'),
     url(r'^empleado/editar/(?P<pk>\d+)/$', login_required(EmpleadoUpdate.as_view()), name='empleado_editar'),
]
