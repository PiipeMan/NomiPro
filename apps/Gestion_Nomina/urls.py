from django.conf.urls import url, include
from apps.Gestion_Nomina.views import PeriodoCreate, PeriodoList, PeriodoUpdate, index
from apps.Gestion_Nomina.views import NominaCreate, NominaList, NominaUpdate
from django.contrib.auth.decorators import login_required


urlpatterns = [
     url(r'^$', index, name='nomina_index'),    
     url(r'^periodo/nuevo/$', login_required(PeriodoCreate.as_view()), name='periodo_crear'),
     url(r'^periodo/ver/$', login_required(PeriodoList.as_view()), name='periodo_listar'),
     url(r'^periodo/editar/(?P<pk>\d+)/$', login_required(PeriodoUpdate.as_view()), name='periodo_editar'),     
     url(r'^nomina/nuevo/$',login_required(NominaCreate.as_view()), name='nomina_crear'),
     url(r'^nomina/ver/$', login_required(NominaList.as_view()), name='nomina_listar'),
     url(r'^nomina/editar/(?P<pk>\d+)/$',login_required(NominaUpdate.as_view()), name='nomina_editar'),     
]
