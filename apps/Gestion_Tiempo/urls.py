from django.conf.urls import url,include
from apps.Gestion_Tiempo.views import ParafiscalesCreate, ParafiscalesList, ParafiscalesUpdate, index
from apps.Gestion_Tiempo.views import DetalleParafiscalesCreate, DetalleParafiscalesList, DetalleParafiscalesUpdate
from apps.Gestion_Tiempo.views import ReporteHorasCreate, ReporteHorasList, ReporteHorasUpdate
from apps.Gestion_Tiempo.views import DetalleHorasCreate, DetalleHorasList, DetalleHorasUpdate
from apps.Gestion_Tiempo.views import HorasAdicionalesCreate, HorasAdicionalesList, HorasAdicionalesUpdate

from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', index, name='index'), 

    url(r'^reportehoras/nuevo/$',login_required(ReporteHorasCreate.as_view()), name='reportehoras_crear'),
    url(r'^reportehoras/ver/$',login_required(ReporteHorasList.as_view()),name='reportehoras_listar'),
    url(r'^reportehoras/editar/(?P<pk>\d+)/$',login_required(ReporteHorasUpdate.as_view()),name='reportehoras_editar'),
    url(r'^horasadicionales/nuevo/$',login_required(HorasAdicionalesCreate.as_view()), name='horasadicionales_crear'),
    url(r'^horasadicionales/ver$',login_required(HorasAdicionalesList.as_view()), name='horasadicionales_listar'),
    url(r'^horasadicionales/editar/(?P<pk>\d+)/$',login_required(HorasAdicionalesUpdate.as_view()),name='horasadicionales_editar'),
    url(r'^parafiscales/nuevo/$', login_required(ParafiscalesCreate.as_view()), name='parafiscales_crear' ),
    url(r'^parafiscales/ver/(?P<pk>\d+)/$',login_required(ParafiscalesUpdate.as_view()),name='parafiscales_editar'),
    url(r'^parafiscales/editar$', login_required(ParafiscalesList.as_view()),name='parafiscales_listar'),
    url(r'^detalleparafiscales/nuevo$', login_required(DetalleParafiscalesCreate.as_view()),name='detalleparafiscal_crear'),
    url(r'^detalleparafiscales/ver$', login_required(DetalleParafiscalesList.as_view()), name='detalleparafiscal_listar'),
    url(r'^detalleparafiscales/editar/(?P<pk>\d+)/$',login_required(DetalleParafiscalesUpdate.as_view()),name='detalleparafiscal_editar'),
    url(r'^detallehoras/nuevo/$',login_required(DetalleHorasCreate.as_view()), name='detallehoras_crear'),
    url(r'^detallehoras/ver/$',login_required(DetalleHorasList.as_view()), name='detallehoras_listar'),
    url(r'^detallehoras/editar/(?P<pk>\d+)/$',login_required(DetalleHorasUpdate.as_view()),name='detallehoras_editar'),
    
     
]
