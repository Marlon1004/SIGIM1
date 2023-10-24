from django.template.loader import get_template
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from investigadores.models import grupos_de_investigacion, investigadores, proyecto_Innovacion
from django.contrib.auth import views as auth_views
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders





#---------------renderizado------------------------------------------------------

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.http import HttpResponse


class LoginViewPlugin(CMSPluginBase):
    #model = YourModel  # Reemplaza "YourModel" con el modelo vinculado a la página personalizada
    render_template = "login.html"  # La plantilla con el formulario de inicio de sesión

    def render(self, context, instance, placeholder):
        # Aquí puedes poner la lógica de tu login_view
        if context['request'].method == 'POST':
            username = context['request'].POST['email']
            password = context['request'].POST['password']
            user = authenticate(context['request'], username=username, password=password)
            if user is not None:
                login(context['request'], user)
                return redirect('accounts/login/')  # Reemplaza esto por la URL a la que deseas redirigir tras el inicio de sesión
            else:
                messages.error(context['request'], 'Usuario o contraseña inválidos')

        return render('login.html')

plugin_pool.register_plugin(LoginViewPlugin)




#c------------creo la vista del login llamado normal--------------------------------------------------------------------

@login_required()
def index(request):
    return render(request, "plantilla/base.html")



#-----------------------------------------------------------------------------------------------------------------


def login_view2(request):
    if request.method == 'POST':

        if request.POST.get('submit') == 'sign_up':

            username = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')

            if User.objects.filter(email=email).exists():  # Condición para la misma identificación de correo electrónico si ya existe
                messages.warning(request, 'Email already exists')
            else:
                user = User(email=email, password=password, username=username)
                user.set_password(password)  # dado que las contraseñas sin procesar no se guardan, por lo tanto, debe configurarse en este método
                user.save()
                messages.success(request,
                                 'User has been registered successfully')  # Muestra mensaje de que el usuario ha sido registrado
            return redirect('login')

        elif request.POST.get('loginsubmit') == 'sign_in':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.warning(request, 'Invalid credentials')
        # print(email,password,username)

    return render(request, 'templates/login1.html')





#---------------------------------------------creacion de pdf------------------------------------------


class SaleInvoicePdfView(View):
    def get(self, request, *args, **kwards):

        template = get_template("templates/proyecto_cientifico.html")
        context = {'title': 'Mi primer pdf Marlon'}
        html=template.render(context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'

        pisa_status = pisa.CreatePDF(
            html, dest=response)
        # if error then show some funny view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')

        return  response



#-----------------------------enviar correos-------------------------------------------------------


from django.core.mail import send_mail
from django.contrib.auth.models import User

def enviar_correo_usuario(request, user_id):
    user = User.objects.get(pk=user_id)

    subject = 'InnoSoft entrega tus Credenciales de acceso a SIGIM'
    message = f'Hola {user.username},\n\nTu usuario: {user.username}\nTu contraseña: {user.password}\n\n¡Bienvenido a nuestro sitio web SIGIM creado por InnoSoft!'
    from_email = 'noreply@tu_sitio.com'
    recipient_list = [user.email]
    message_encoded = message.encode('utf-8')
    send_mail(subject, message, from_email, recipient_list)




#-----------------------------creacon de pdf 2 funciona-------------------------------------------------------

from django.shortcuts import render
from reportlab.pdfgen import canvas
from sekizai.context import SekizaiContext
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, PageTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Image
from reportlab.platypus import BaseDocTemplate
from reportlab.platypus import PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from django.templatetags.static import static



def header(canvas, doc):
    width, height = letter

    # Agregar el título en el centro
    styles = getSampleStyleSheet()
    canvas.setFont("Helvetica-Bold", 12)
    canvas.drawString(width / 2 - 30, height - 30, "Título del Documento")

    # Agregar un encabezado personalizado
    #canvas.setFont("Helvetica", 10)
    #canvas.drawString(width / 2 - 30, height - 50, "Encabezado Personalizado")


def generar_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="documento.pdf"'

    doc = SimpleDocTemplate(response, pagesize=letter)

    # Crear una plantilla de página con el encabezado personalizado
    page_template = PageTemplate(id='page', onPage=header)
    doc.addPageTemplates([page_template])

    story = []

    # Agregar contenido al cuerpo del PDF (por ejemplo, tu texto principal)
    story.append("¡Hola, este es un PDF generado con ReportLab en Django CMS!")

    doc.build(story)



    return response


#-----------------------------creacon de pdf 2 funciona-------------------------------------------------------------------------

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from sekizai.context import SekizaiContext


def generar_pdf2(request):
    template = get_template('../templates/proyecto_innovacion.html')
    context = {'titulo': 'Título del Documento', 'contenido': 'Contenido del documento...'}
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="documento.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error al generar PDF', status=500)

    return response


#-----------------------------Envio de datos de primer proyecto-------------------------------------------------------------------------

from django.shortcuts import render, redirect
from investigadores.models import ModeloPrueba, proyecto_Tecnologico  # Importa el modelo necesario


def guardar_datos(request):
    if request.method == 'POST':

        nombre_proyecto = request.POST['nombre_proyecto']
        palabras_claves = request.POST['palabras_claves']
        nombre_de_convocatoria = request.POST['nombre_de_convocatoria']
        tiempo_en_meses = request.POST['tiempo_en_meses']
        Lugar_Ejecucion = request.POST['Lugar_Ejecucion']
        tecnologia_convergentes_e_industrias = request.POST.get('tecnologia_convergentes_e_industrias')
        biotecnologia_bioeconomia_economia = request.POST.get('biotecnologia_bioeconomia_economia')
        industrias_creativas_culturales = request.POST.get('industrias_creativas_culturales')
        energias_sostenibles_economia_circular = request.POST.get('energias_sostenibles_economia_circular')
        innovacion_salud_bienestar = request.POST.get('innovacion_salud_bienestar')
        conocimiento_educacion_para_inclusion = request.POST.get('conocimiento_educacion_para_inclusion')
        promocion_de_productividad = request.POST.get('conocimiento_educacion_para_inclusion')
        automatizacion_de_produccion = request.POST.get('automatizacion_de_produccion')
        diversificacion_en_presentaciones = request.POST.get('diversificacion_en_presentaciones')
        pulverizadora_de_leche_polvo = request.POST.get('pulverizadora_de_leche_polvo')
        factibilidad_de_planta_concentrados = request.POST.get('factibilidad_de_planta_concentrados')
        mejoramiento_estatus_sanitario_bovino = request.POST.get('mejoramiento_estatus_sanitario_bovino')
        erradicacion_disminucion_de_punta_morada = request.POST.get('erradicacion_disminucion_de_punta_morada')
        disminucion_de_costos = request.POST.get('disminucion_de_costos')
        txt_nombre_InvestigadorP = request.POST.get('txt_nombre_InvestigadorP')
        txt_documentoIdentidad_InvestigadorP = request.POST.get('txt_documentoIdentidad_InvestigadorP')
        txt_grupoInvestigacion_InvestigadorP = request.POST.get('txt_grupoInvestigacion_InvestigadorP')
        txt_nivelEstudio_investigadorP = request.POST.get('txt_nivelEstudio_investigadorP')
        txt_institucionVinculado_InvestigadorP = request.POST.get('txt_institucionVinculado_InvestigadorP')
        txt_funciones_InvestigadorP = request.POST.get('txt_funciones_InvestigadorP')
        txt_dedicacionSemanal_InvestigadorP = request.POST.get('txt_dedicacionSemanal_InvestigadorP')
        txt_nombre_InvestigadorInterno = request.POST.get('txt_nombre_InvestigadorInterno')
        txt_documentoIdentidad_InvestigadorInterno = request.POST.get('txt_documentoIdentidad_InvestigadorInterno')
        txt_grupoInvestigacion_InvestigadorInterno = request.POST.get('txt_grupoInvestigacion_InvestigadorInterno')
        txt_nivelEstudio_investigadorInterno = request.POST.get('txt_nivelEstudio_investigadorInterno')
        txt_institucionVinculado_InvestigadorInterno = request.POST.get('txt_institucionVinculado_InvestigadorInterno')
        txt_funciones_InvestigadorInterno = request.POST.get('txt_funciones_InvestigadorInterno')
        txt_dedicacionSemanal_InvestigadorInterno = request.POST.get('txt_dedicacionSemanal_InvestigadorInterno')
        txt_nombre_InvestigadorExterno = request.POST.get('txt_nombre_InvestigadorExterno')
        txt_documentoIdentidad_InvestigadorExterno = request.POST.get('txt_documentoIdentidad_InvestigadorExterno')
        txt_grupoInvestigacion_InvestigadorExterno = request.POST.get('txt_grupoInvestigacion_InvestigadorExterno')
        txt_nivelEstudio_investigadorExterno = request.POST.get('txt_nivelEstudio_investigadorExterno')
        txt_institucionVinculado_InvestigadorExterno = request.POST.get('txt_institucionVinculado_InvestigadorExterno')
        txt_funciones_InvestigadorExterno = request.POST.get('txt_funciones_InvestigadorExterno')
        txt_dedicacionSemanal_InvestigadorExterno = request.POST.get('txt_dedicacionSemanal_InvestigadorExterno')
        txt_nombre_Auxiliar_Interno1 = request.POST.get('txt_nombre_Auxiliar_Interno1')
        txt_documentoIdentidad_Auxliar_Interno1 = request.POST.get('txt_documentoIdentidad_Auxliar_Interno1')
        txt_codigoEstudiantil = request.POST.get('txt_codigoEstudiantil')
        txt_institucionVinculado_Auxliar_Interno1 = request.POST.get('txt_institucionVinculado_Auxliar_Interno1')
        txt_funciones_Auxliar_Interno1 = request.POST.get('txt_funciones_Auxliar_Interno1')
        txt_dedicacionSemanal_Auxliar_Interno1 = request.POST.get('txt_dedicacionSemanal_Auxliar_Interno1')
        txt_nombre_Auxiliar_externo = request.POST.get('txt_nombre_Auxiliar_externo')
        txt_documentoIdentidad_Auxiliar_externo = request.POST.get('txt_documentoIdentidad_Auxiliar_externo')
        txt_codigoEstudiantil_Coinvestigador = request.POST.get('txt_codigoEstudiantil_Coinvestigador')
        txt_institucionVinculado_Auxiliar_externo = request.POST.get('txt_institucionVinculado_Auxiliar_externo')
        txt_funciones_Auxiliar_externo = request.POST.get('txt_funciones_Auxiliar_externo')
        txt_dedicacionSemanal_Auxiliar_externo = request.POST.get('txt_dedicacionSemanal_Auxiliar_externo')
        txt_4resumen_ejecutivo = request.POST.get('txt_4resumen_ejecutivo')
        txt_5objetivos = request.POST.get('txt_5objetivos')
        txt_6descripcion = request.POST.get('txt_6descripcion')
        txt_7justificacion = request.POST.get('txt_7justificacion')
        txt_8marcoConceptual = request.POST.get('txt_8marcoConceptual')
        txt_8antecedentes = request.POST.get('txt_8antecedentes')
        txt_10novedadProyecto = request.POST.get('txt_10novedadProyecto')
        txt_11metodologia = request.POST.get('txt_11metodologia')
        txt_14componente_etico = request.POST.get('txt_14componente_etico')
        txt_15identidad = request.POST.get('txt_15identidad')
        txt_17alineacion = request.POST.get('txt_17alineacion')
        text_presupuesto = request.POST.get('text_presupuesto')
        txt_actividad1_Objetivo1 = request.POST.get('txt_actividad1_Objetivo1')
        txt_producto1_Objetivo1 = request.POST.get('txt_producto1_Objetivo1')
        txt_mes1_Objetivo1 = request.POST.get('txt_mes1_Objetivo1')
        txt_actividad2_Objetivo1 = request.POST.get('txt_actividad2_Objetivo1')
        txt_producto2_Objetivo1 = request.POST.get('txt_producto2_Objetivo1')
        txt_mes2_Objetivo1 = request.POST.get('txt_mes2_Objetivo1')
        txt_actividad3_Objetivo1 = request.POST.get('txt_actividad3_Objetivo1')
        txt_producto3_Objetivo1 = request.POST.get('txt_producto3_Objetivo1')
        txt_mes3_Objetivo1 = request.POST.get('txt_mes3_Objetivo1')
        txt_actividad1_Objetivo2 = request.POST.get('txt_actividad1_Objetivo2')
        txt_producto1_Objetivo2 = request.POST.get('txt_producto1_Objetivo2')
        txt_mes1_Objetivo2 = request.POST.get('txt_mes1_Objetivo2')
        txt_actividad2_Objetivo2 = request.POST.get('txt_actividad2_Objetivo2')
        txt_producto2_Objetivo2 = request.POST.get('txt_producto2_Objetivo2')
        txt_mes2_Objetivo2 = request.POST.get('txt_mes2_Objetivo2')
        txt_actividad3_Objetivo2 = request.POST.get('txt_actividad3_Objetivo2')
        txt_producto3_Objetivo2 = request.POST.get('txt_producto3_Objetivo2')
        txt_mes3_Objetivo2 = request.POST.get('txt_mes3_Objetivo2')
        txt_entregainformeavance = request.POST.get('txt_entregainformeavance')
        txt_actividad1_Objetivo3 = request.POST.get('txt_actividad1_Objetivo3')
        txt_producto1_Objetivo3 = request.POST.get('txt_producto1_Objetivo3')
        txt_mes1_Objetivo3 = request.POST.get('txt_mes1_Objetivo3')
        txt_actividad2_Objetivo3 = request.POST.get('txt_actividad2_Objetivo3')
        txt_producto2_Objetivo3 = request.POST.get('txt_producto2_Objetivo3')
        txt_mes2_Objetivo3 = request.POST.get('txt_mes2_Objetivo3')
        txt_actividad3_Objetivo3 = request.POST.get('txt_actividad3_Objetivo3')
        txt_producto3_Objetivo3 = request.POST.get('txt_producto3_Objetivo3')
        txt_mes3_Objetivo3 = request.POST.get('txt_mes3_Objetivo3')
        txt_actividad4_Objetivo3 = request.POST.get('txt_actividad4_Objetivo3')
        txt_producto4_Objetivo3 = request.POST.get('txt_producto4_Objetivo3')
        txt_mes4_Objetivo3 = request.POST.get('txt_mes4_Objetivo3')
        txt_productos_Estrategiadivulgacion = request.POST.get('txt_productos_Estrategiadivulgacion')
        txt_entregainformafinal = request.POST.get('txt_entregainformafinal')
        txt_referecias = request.POST.get('txt_referecias')
        txt_campoAcademico_Indicador = request.POST.get('txt_campoAcademico_Indicador')
        txt_desarrolloTecnologico_Indicador = request.POST.get('txt_desarrolloTecnologico_Indicador')
        txt_social_Indicador = request.POST.get('txt_social_Indicador')
        txt_educativo_Indicador = request.POST.get('txt_educativo_Indicador')
        txt_simbolico_Indicador = request.POST.get('txt_simbolico_Indicador')
        txt_economicos_Indicador = request.POST.get('txt_economicos_Indicador')
        # Procesa más campos aquí

        # Crea una instancia del modelo y guarda los datos
        nuevo_registro = proyecto_Tecnologico(nombre_proyecto= nombre_proyecto, palabras_claves= palabras_claves, nombre_de_convocatoria = nombre_de_convocatoria, tiempo_en_meses= tiempo_en_meses, Lugar_Ejecucion=Lugar_Ejecucion, tecnologia_convergentes_e_industrias=tecnologia_convergentes_e_industrias,
                                              biotecnologia_bioeconomia_economia=biotecnologia_bioeconomia_economia, industrias_creativas_culturales=industrias_creativas_culturales, energias_sostenibles_economia_circular=energias_sostenibles_economia_circular, innovacion_salud_bienestar=innovacion_salud_bienestar, conocimiento_educacion_para_inclusion=conocimiento_educacion_para_inclusion, promocion_de_productividad=promocion_de_productividad,
                                              automatizacion_de_produccion=automatizacion_de_produccion, diversificacion_en_presentaciones=diversificacion_en_presentaciones, pulverizadora_de_leche_polvo=pulverizadora_de_leche_polvo, factibilidad_de_planta_concentrados=factibilidad_de_planta_concentrados, mejoramiento_estatus_sanitario_bovino=mejoramiento_estatus_sanitario_bovino, erradicacion_disminucion_de_punta_morada=erradicacion_disminucion_de_punta_morada,
                                              disminucion_de_costos=disminucion_de_costos, txt_nombre_InvestigadorP=txt_nombre_InvestigadorP, txt_documentoIdentidad_InvestigadorP=txt_documentoIdentidad_InvestigadorP, txt_grupoInvestigacion_InvestigadorP=txt_grupoInvestigacion_InvestigadorP, txt_nivelEstudio_investigadorP=txt_nivelEstudio_investigadorP,
                                              txt_institucionVinculado_InvestigadorP=txt_institucionVinculado_InvestigadorP, txt_funciones_InvestigadorP=txt_funciones_InvestigadorP, txt_dedicacionSemanal_InvestigadorP=txt_dedicacionSemanal_InvestigadorP, txt_nombre_InvestigadorInterno=txt_nombre_InvestigadorInterno,
                                              txt_documentoIdentidad_InvestigadorInterno=txt_documentoIdentidad_InvestigadorInterno, txt_grupoInvestigacion_InvestigadorInterno=txt_grupoInvestigacion_InvestigadorInterno, txt_nivelEstudio_investigadorInterno=txt_nivelEstudio_investigadorInterno, txt_institucionVinculado_InvestigadorInterno=txt_institucionVinculado_InvestigadorInterno,
                                              txt_funciones_InvestigadorInterno=txt_funciones_InvestigadorInterno, txt_dedicacionSemanal_InvestigadorInterno=txt_dedicacionSemanal_InvestigadorInterno, txt_nombre_InvestigadorExterno=txt_nombre_InvestigadorExterno, txt_documentoIdentidad_InvestigadorExterno=txt_documentoIdentidad_InvestigadorExterno, txt_grupoInvestigacion_InvestigadorExterno=txt_grupoInvestigacion_InvestigadorExterno, txt_nivelEstudio_investigadorExterno=txt_nivelEstudio_investigadorExterno,
                                              txt_institucionVinculado_InvestigadorExterno=txt_institucionVinculado_InvestigadorExterno, txt_funciones_InvestigadorExterno=txt_funciones_InvestigadorExterno, txt_dedicacionSemanal_InvestigadorExterno=txt_dedicacionSemanal_InvestigadorExterno, txt_nombre_Auxiliar_Interno1=txt_nombre_Auxiliar_Interno1,
                                              txt_documentoIdentidad_Auxliar_Interno1=txt_documentoIdentidad_Auxliar_Interno1, txt_codigoEstudiantil=txt_codigoEstudiantil, txt_institucionVinculado_Auxliar_Interno1=txt_institucionVinculado_Auxliar_Interno1, txt_funciones_Auxliar_Interno1=txt_funciones_Auxliar_Interno1, txt_dedicacionSemanal_Auxliar_Interno1=txt_dedicacionSemanal_Auxliar_Interno1, txt_nombre_Auxiliar_externo=txt_nombre_Auxiliar_externo,
                                              txt_documentoIdentidad_Auxiliar_externo=txt_documentoIdentidad_Auxiliar_externo, txt_codigoEstudiantil_Coinvestigador=txt_codigoEstudiantil_Coinvestigador, txt_institucionVinculado_Auxiliar_externo=txt_institucionVinculado_Auxiliar_externo,
                                              txt_funciones_Auxiliar_externo=txt_funciones_Auxiliar_externo, txt_dedicacionSemanal_Auxiliar_externo=txt_dedicacionSemanal_Auxiliar_externo,  txt_4resumen_ejecutivo=txt_4resumen_ejecutivo,
                                              txt_5objetivos=txt_5objetivos, txt_6descripcion=txt_6descripcion, txt_7justificacion=txt_7justificacion, txt_8marcoConceptual=txt_8marcoConceptual, txt_8antecedentes=txt_8antecedentes,
                                              txt_10novedadProyecto=txt_10novedadProyecto, txt_11metodologia=txt_11metodologia, txt_14componente_etico=txt_14componente_etico, txt_15identidad=txt_15identidad,
                                              txt_17alineacion=txt_17alineacion, text_presupuesto=text_presupuesto, txt_actividad1_Objetivo1=txt_actividad1_Objetivo1, txt_producto1_Objetivo1=txt_producto1_Objetivo1,
                                              txt_mes1_Objetivo1=txt_mes1_Objetivo1, txt_actividad2_Objetivo1=txt_actividad2_Objetivo1, txt_producto2_Objetivo1=txt_producto2_Objetivo1, txt_mes2_Objetivo1=txt_mes2_Objetivo1,
                                              txt_actividad3_Objetivo1=txt_actividad3_Objetivo1, txt_producto3_Objetivo1=txt_producto3_Objetivo1, txt_mes3_Objetivo1=txt_mes3_Objetivo1, txt_actividad1_Objetivo2=txt_actividad1_Objetivo2,
                                              txt_producto1_Objetivo2=txt_producto1_Objetivo2, txt_mes1_Objetivo2=txt_mes1_Objetivo2, txt_actividad2_Objetivo2=txt_actividad2_Objetivo2, txt_producto2_Objetivo2=txt_producto2_Objetivo2,
                                              txt_mes2_Objetivo2=txt_mes2_Objetivo2, txt_actividad3_Objetivo2=txt_actividad3_Objetivo2, txt_producto3_Objetivo2=txt_producto3_Objetivo2, txt_mes3_Objetivo2=txt_mes3_Objetivo2,
                                              txt_entregainformeavance=txt_entregainformeavance, txt_actividad1_Objetivo3=txt_actividad1_Objetivo3, txt_producto1_Objetivo3=txt_producto1_Objetivo3, txt_mes1_Objetivo3=txt_mes1_Objetivo3,
                                              txt_actividad2_Objetivo3=txt_actividad2_Objetivo3, txt_producto2_Objetivo3=txt_producto2_Objetivo3, txt_mes2_Objetivo3=txt_mes2_Objetivo3, txt_actividad3_Objetivo3=txt_actividad3_Objetivo3,
                                              txt_producto3_Objetivo3=txt_producto3_Objetivo3, txt_mes3_Objetivo3=txt_mes3_Objetivo3, txt_actividad4_Objetivo3=txt_actividad4_Objetivo3, txt_producto4_Objetivo3=txt_producto4_Objetivo3,
                                              txt_mes4_Objetivo3=txt_mes4_Objetivo3, txt_productos_Estrategiadivulgacion=txt_productos_Estrategiadivulgacion, txt_entregainformafinal=txt_entregainformafinal, txt_referecias=txt_referecias,
                                              txt_campoAcademico_Indicador=txt_campoAcademico_Indicador, txt_desarrolloTecnologico_Indicador=txt_desarrolloTecnologico_Indicador, txt_social_Indicador=txt_social_Indicador, txt_educativo_Indicador=txt_educativo_Indicador,
                                              txt_simbolico_Indicador=txt_simbolico_Indicador, txt_economicos_Indicador=txt_economicos_Indicador)
        nuevo_registro.save()
        return redirect('/exitoso/')  # Redirige a una página exitosa
    return render(request, 'prueba-datos.html')