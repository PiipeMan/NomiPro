from django.shortcuts import render, redirect
from apps.Gestion_Tiempo.forms import ParafiscalesForm, DetalleHorasForm, DetalleParafiscalesForm, HorasAdicionalesForm, ReporteHorasForm
from apps.Gestion_Tiempo.models import  Parafiscales, HorasAdicionales, ReporteHoras, DetalleHoras, DetalleParafiscales
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy


# Create your views here.
#index 
def index(request):
   return render(request,"base/base.html")
   
class ParafiscalesCreate(CreateView):
  model=Parafiscales
  template_name='Gestion_Tiempos/parafiscales_form.html'
  form_class=ParafiscalesForm
  success_url=reverse_lazy('parafiscales_listar')

class ParafiscalesList(ListView):
   model=Parafiscales
   template_name='Gestion_Tiempos/parafiscales_list.html'

class ParafiscalesUpdate(UpdateView):
   model=Parafiscales
   form_class=ParafiscalesForm
   template_name='Gestion_Tiempos/parafiscales_form.html'
   success_url=reverse_lazy('parafiscales_listar')

class DetalleParafiscalesCreate(CreateView):
   model=DetalleParafiscales
   template_name='Gestion_Tiempos/detalle_parafiscales_form.html'
   form_class=ParafiscalesForm
   success_url=reverse_lazy('detalle_parafiscales_listar')

class DetalleParafiscalesList(ListView):
   model=DetalleParafiscales
   template_name='Gestion_Tiempos/detalle_parafiscales_list.html'

class DetalleParafiscalesUpdate(UpdateView):
   model=DetalleParafiscales
   form_class=DetalleParafiscalesForm
   template_name='Gestion_Tiempos/detalle_parafiscales_form.html'
   success_url=reverse_lazy('detalle_parafiscales_listar')

class ReporteHorasCreate(CreateView):
   model=ReporteHoras
   template_name='Gestion_Tiempos/reportehoras_form.html'
   form_class=ReporteHorasForm
   success_url=reverse_lazy('reportehoras_listar')

class ReporteHorasList(ListView):
   model=ReporteHoras
   template_name='Gestion_Tiempos/reportehoras_list.html'

class ReporteHorasUpdate(UpdateView):
   model=ReporteHoras
   template_name='Gestion_Tiempos/reportehoras_list.html'
   form_class=ReporteHorasForm
   success_url=reverse_lazy('reportehoras_listar')

class DetalleHorasCreate(CreateView):
   model=DetalleHoras
   template_name='Gestion_Tiempos/detallehoras_form.html'
   form_class=DetalleHorasForm
   success_url=reverse_lazy('detallehoras_listar')

class DetalleHorasList(ListView):
   model=DetalleHoras
   template_name='Gestion_Tiempos/detallehoras_list.html'

class DetalleHorasUpdate(UpdateView):
   model=DetalleHoras
   template_name='Gestion_Tiempos/detallehoras_list.html'
   form_class=DetalleHorasForm
   success_url=reverse_lazy('detallehoras_listar')

class HorasAdicionalesCreate(CreateView):
   model=HorasAdicionales
   template_name='Gestion_Tiempos/horasadicionales_form.html'
   form_class=HorasAdicionalesForm
   success_url=reverse_lazy('horasadicionales_listar')

class HorasAdicionalesList(ListView):
   model=HorasAdicionales
   template_name='Gestion_Tiempos/horasadicionales_list.html'

class HorasAdicionalesUpdate(UpdateView):
   model=HorasAdicionales
   template_name='Gestion_Tiempos/horasadicionales_list.html'
   form_class=HorasAdicionalesForm
   success_url=reverse_lazy('horasadicionales_listar')