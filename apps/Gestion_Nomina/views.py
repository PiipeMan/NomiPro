from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from apps.Gestion_Nomina.forms import PeriodoForm, NominaForm
from apps.Gestion_Nomina.models import Periodo, Nomina
from apps.Gestion_Empleado.models import Empleado, Cargo
from apps.Gestion_Tiempo.models import Parafiscales, HorasAdicionales, Cargo
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.contrib import messages
from django.urls import reverse_lazy


# Create your views here.
#index 
def index(request):
   return render(request,"base/base.html")
   
class PeriodoCreate(CreateView):
   model= Periodo
   form_class= PeriodoForm
   template_name='Gestion_Nomina/periodo_form.html'  
   success_url=reverse_lazy('periodo_listar')

class PeriodoList(ListView):
   model= Periodo
   template_name='Gestion_Nomina/periodo_list.html'

class PeriodoUpdate(UpdateView):
   model= Periodo
   form_class= PeriodoForm
   template_name='Gestion_Nomina/periodo_form.html'
   success_url=reverse_lazy('periodo_listar')

class NominaCreate(CreateView):
   model= Nomina
   form_class= NominaForm
   template_name='Gestion_Nomina/nomina_form.html' 
   context_object_name='obj' 
   success_url=reverse_lazy('nomina_listar')

   def get_context_data(self, **kwargs):
      context = super(NominaCreate, self).get_context_data(**kwargs)
      context['form2'] = Parafiscales.objects.all()
      context['form3'] = HorasAdicionales.objects.all()
      context['form4'] = Cargo.objects.all()
      if 'form' not in context:
         context['form'] = self.form_class(self.request.GET)

      return context
   def post(self, request, *args, **kwargs):
      self.object = self.get_object
      form = self.form_class(request.POST)
      if request.method=='POST':
         if form.is_valid():
            Nomina = form.save(commit=False)
            Nomina.Valor_Pagar = request.POST.get("id_valorpagar2")
            Nomina.Subtotal = request.POST.get("id_subtotal")
            Nomina.Total = request.POST.get("id_total")
            Nomina = form.save()
            Nomina.save()
            return HttpResponseRedirect(self.get_success_url())
         else:
            return self.render_to_response(self.get_context_data(form=form))



class NominaList(ListView):
   model= Nomina
   template_name='Gestion_Nomina/nomina_list.html'

class NominaUpdate(UpdateView):
   model= Nomina
   form_class= NominaForm
   template_name='Gestion_Nomina/nomina_form.html'   
   success_url=reverse_lazy('nomina_listar')