from django.shortcuts import render
from django.views.generic import FormView, CreateView,  ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy 
from .models import Nino, Inventario, Eventos, Solicitudes, Expendiente_medico, Expendiente_escolar
# Create your views here.

def vist(request):
	return render(request, 'CunaAngeles/example.html')

def adminnistrador(request):
	return render(request, 'CunaAngeles/administrador.html')
	

def expediente(request):
	return render(request, 'CunaAngeles/expediente.html')


def editar(request):
	return render(request, 'CunaAngeles/editar.html')

def eliminar(request):
	return render(request, 'CunaAngeles/eliminar.html')


def expediente_registro(request):
	return render(request, 'CunaAngeles/registro_expediente.html')

class Solicitudes_registros(CreateView):
	template_name='CunaAngeles/example.html'
	model = Solicitudes
	fields=['nombre','correo','solicitud','comentario']
	success_url=reverse_lazy('solicitudes') 

	def post(self, request, *args, **kwargs):
		flag = False
		p = Solicitudes()
		p.nombre = request.POST['nombre']
		p.correo = request.POST['correo']
		p.solicitud = request.POST['solicitud']
		p.comentario = request.POST['comentario']

		p.save()
		flag = True

		return render(request,'CunaAngeles/example.html', {'flag':flag})


class Nino_registros(CreateView):
	template_name='CunaAngeles/registro_nino.html'
	model = Nino
	fields=['nombre','apellidos','edad','fechaNaci','fechaRegis']
	success_url=reverse_lazy('registroNino') 

	def post(self, request, *args, **kwargs):
		flag = False
		p = Nino()
		p.nombre = request.POST['nombre']
		p.apellidos = request.POST['apellidos']
		p.edad = request.POST['edad']
		p.fechaNaci = request.POST['fechaNaci']
		p.fechaRegis = request.POST['fechaRegis']
		
		p.save()
		flag = True

		return render(request,'CunaAngeles/registro_nino.html', {'flag':flag})

class Expedientes_medi_Registro(CreateView):
	template_name='CunaAngeles/registro_expediente_medico.html'
	model = Expendiente_medico
	fields='__all__'
	success_url=reverse_lazy('expedientesregisMedico') 

	def get_context_data(self, **kwargs):
		ctx = super(Expedientes_medi_Registro, self).get_context_data(**kwargs)
		ctx['objects_list'] = Nino.objects.all()
		return ctx

	def post(self, request, *args, **kwargs):
		flag = False
		p = Expendiente_medico()
		p.nino = request.POST['nino']
		p.alergia = request.POST['alergia']
		p.peso = request.POST['peso']
		p.enfermedades_hereditarias = request.POST['enfermedades_hereditarias']
		p.comentario = request.POST['comentario']
		
		p.save()
		flag = True

		return render(request,'CunaAngeles/registro_expediente_medico.html', {'flag':flag})



class Expedientes_Esco_Registro(CreateView):
	template_name='CunaAngeles/registro_expediente_escolar.html'
	model = Expendiente_escolar
	fields='__all__'
	success_url=reverse_lazy('expedientesEscolar')

	def get_context_data(self, **kwargs):
		ctx = super(Expedientes_Esco_Registro, self).get_context_data(**kwargs)
		ctx['objects_list'] = Nino.objects.all()
		return ctx
	
	def post(self, request, *args, **kwargs):
		flag = False
		p = Expendiente_escolar()
		p.nino = request.POST['nino']
		p.aescolaridad = request.POST['escolaridad']
		p.tutor = request.POST['tutor']
		p.hora_entrada = request.POST['hora_entrada']
		p.hora_salida  = request.POST['hora_salida ']
		p.comentario = request.POST['comentario']
		p.edad = request.POST['edad']
		
		p.save()
		flag = True

		return render(request,'CunaAngeles/registro_nino.html', {'flag':flag}) 


class Eventos_registros(CreateView):
	template_name='CunaAngeles/registro_eventos.html'
	model = Eventos
	fields=['nombre','lugar','fecha','hora','patrocinadores']
	success_url=reverse_lazy('registroEventos') 

	def post(self, request, *args, **kwargs):
		flag = False
		p = Eventos()
		p.nombre = request.POST['nombre']
		p.lugar = request.POST['lugar']
		p.fecha = request.POST['fecha']
		p.hora = request.POST['hora']
		p.patrocinadores = request.POST['patrocinadores']
		
		p.save()
		flag = True

		return render(request,'CunaAngeles/registro_eventos.html', {'flag':flag})


class Inventario_registros(CreateView):
	template_name='CunaAngeles/inventario.html'
	model = Inventario
	fields=['nombre','fechaRegistrada','fechaCaducacion']
	success_url=reverse_lazy('Inventario') 
	
	def post(self, request, *args, **kwargs):
		flag = False
		p = Inventario()
		p.nombre = request.POST['nombre']
		p.fechaRegistrada = request.POST['fechaRegistrada']
		p.fechaCaducacion = request.POST['fechaCaducacion']
		
		p.save()
		flag = True

		return render(request,'CunaAngeles/Inventario.html', {'flag':flag})

	


class Eventos_Report(ListView):
	template_name='CunaAngeles/eventos.html'
	model = Eventos

class Ninos_Report(ListView):
	template_name='CunaAngeles/ninosperfil.html'
	model = Nino
	
 
class Expedientes_Esco(ListView):
	template_name='CunaAngeles/expedienteescolar.html'
	model = Expendiente_escolar


class Expendiente_medi(ListView):
	template_name='CunaAngeles/expedientesmedico.html'
	model = Expendiente_medico


class ninos_editar(ListView):
	template_name='CunaAngeles/Editar/ninos_editar.html'
	model = Nino

class eventos_editar(ListView):
	template_name='CunaAngeles/Editar/eventos_editar.html'
	model = Eventos

class ex_medico_editar(ListView):
	template_name='CunaAngeles/Editar/medico_editar.html'
	model = Expendiente_medico

class ex_escolar_editar(ListView):
	template_name='CunaAngeles/Editar/escolar_editar.html'
	model = Expendiente_escolar

class inventario_editar(ListView):
	template_name='CunaAngeles/Editar/inventario_editar.html'
	model = Inventario

class update_ninos(UpdateView):
	model = Nino
	fields = ['nombre','apellidos','edad','fechaNaci','fechaRegis']
	template_name = 'CunaAngeles/Update/update_ninos.html'
	success_url = reverse_lazy('editar')

class update_eventos(UpdateView):
	model = Eventos
	fields = '__all__'
	template_name = 'CunaAngeles/Update/update_eventos.html'
	success_url = reverse_lazy('editar')

class update_inventario(UpdateView):
	model = Inventario
	fields = '__all__'
	template_name = 'CunaAngeles/Update/update_inventario.html'
	success_url = reverse_lazy('editar')

class update_exp_medico(UpdateView):
	model = Expendiente_medico
	fields = '__all__'
	template_name = 'CunaAngeles/Update/update_medico.html'
	success_url = reverse_lazy('editar')

class update_exp_escolar(UpdateView):
	model =  Expendiente_escolar
	fields = '__all__'
	template_name = 'CunaAngeles/Update/update_escolar.html'
	success_url = reverse_lazy('editar')



class ninos_eliminar(ListView):
	template_name='CunaAngeles/Delete/ninos_eliminar.html'
	model = Nino

class eventos_eliminar(ListView):
	template_name='CunaAngeles/Delete/eventos_eliminar.html'
	model = Eventos

class ex_medico_eliminar(ListView):
	template_name='CunaAngeles/Delete/medico_eliminar.html'
	model = Expendiente_medico

class ex_escolar_eliminar(ListView):
	template_name='CunaAngeles/Delete/escolar_eliminar.html'
	model = Expendiente_escolar

class inventario_eliminar(ListView):
	template_name='CunaAngeles/Delete/inventario_eliminar.html'
	model = Inventario




class delete_nino(DeleteView):
	model =  Nino
	template_name = 'CunaAngeles/Delete/delete_nino.html'
	success_url = reverse_lazy('eliminar')