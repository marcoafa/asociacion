from django.conf.urls import url
from .views import vist, adminnistrador, expediente, Nino_registros, Eventos_registros, Inventario_registros, Solicitudes_registros, Eventos_Report, Ninos_Report, Expedientes_Esco, Expendiente_medi,expediente_registro , Expedientes_Esco_Registro, Expedientes_medi_Registro, editar,  update_ninos, ninos_editar, eventos_editar, inventario_editar, ex_medico_editar, ex_escolar_editar, update_eventos, update_inventario, update_exp_medico, update_exp_escolar, eliminar, delete_nino, ninos_eliminar, eventos_eliminar,  ex_medico_eliminar,  ex_escolar_eliminar, inventario_eliminar

urlpatterns = [
	url(r'^$', Solicitudes_registros.as_view(), name='inicio'),
	url(r'^administrador/$', adminnistrador, name='administrador'),
	url(r'^expediente/$', expediente, name='expediente'),
	url(r'^registroNino/$', Nino_registros.as_view(), name='registroNino'),
	url(r'^registroEventos/$', Eventos_registros.as_view(), name='registroEventos'),
	url(r'^inventario/$', Inventario_registros.as_view(), name='inventario'),
	url(r'^eventos/$', Eventos_Report.as_view(), name='eventos'),
	url(r'^solicitudes/$', vist, name='solicitudes'),
	url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'CunaAngeles/login.html'}, name='login'),
 	url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
	url(r'^ninos/$', Ninos_Report.as_view(), name='ninos'),
	url(r'^expediente_registro/$', expediente_registro, name='expediente_registro'),
	
	url(r'^expedientesreportEscolar/$', Expedientes_Esco.as_view(), name='expedientesreportEscolar'),
	url(r'^expedientesreportMedico/$', Expendiente_medi.as_view(), name='expedientesreportMedico'),
	url(r'^expedientesregisEscolar/$', Expedientes_Esco_Registro.as_view(), name='expedientesregisEscolar'),
	url(r'^expedientesregisMedico/$', Expedientes_medi_Registro.as_view(), name='expedientesregisMedico'),

	url(r'^editar/$', editar, name='editar'),
	url(r'^update_ninos/(?P<pk>[-\w]+)/$',update_ninos.as_view(), name = 'update_ninos'),
	url(r'^update_eventos/(?P<pk>[-\w]+)/$',update_eventos.as_view(), name = 'update_eventos'),
	url(r'^update_inventario(?P<pk>[-\w]+)/$',update_inventario.as_view(), name = 'update_inventario'),
	url(r'^update_exp_medico/(?P<pk>[-\w]+)/$',update_exp_medico.as_view(), name = 'update_exp_medico'),
	url(r'^update_exp_escolar(?P<pk>[-\w]+)/$',update_exp_escolar.as_view(), name = 'update_exp_escolar'),
	url(r'^ninos_editar/$', ninos_editar.as_view(), name='ninos_editar'),
	url(r'^eventos_editar/$', eventos_editar.as_view(), name='eventos_editar'),
	url(r'^inventario_editar/$', inventario_editar.as_view(), name='inventario_editar'),
	url(r'^ex_medico_editar/$', ex_medico_editar.as_view(), name='ex_medico_editar'),
	url(r'^ex_escolar_editar/$', ex_escolar_editar.as_view(), name='ex_escolar_editar'),

	url(r'^eliminar/$', eliminar, name='eliminar'),
	url(r'^ninos_eliminar/$', ninos_eliminar.as_view(), name='ninos_eliminar'),
	url(r'^eventos_eliminar/$', eventos_eliminar.as_view(), name='eventos_eliminar'),
	url(r'^inventario_eliminar/$', inventario_eliminar.as_view(), name='inventario_eliminar'),
	url(r'^ex_medico_eliminar/$', ex_medico_eliminar.as_view(), name='ex_medico_eliminar'),
	url(r'^ex_escolar_eliminar/$', ex_escolar_eliminar.as_view(), name='ex_escolar_eliminar'),
    url(r'^delete_nino/(?P<pk>[-\w]+)/$',delete_nino.as_view(), name = 'delete_nino'),
	
		
	
]