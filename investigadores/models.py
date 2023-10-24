from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class ModeloPrueba(models.Model):
    nombre = models.CharField(max_length=100)




class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmado = models.BooleanField(default=False)


class grupos_de_investigacion(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField("Codigo", max_length=10)
    nombre_Grupo = models.CharField("Nombre del Grupo", max_length=70)
    area_Conocimiento = models.CharField("Area Conocimiento", max_length=50)
    clasificacion_MinCiencias = models.CharField("Clasificación MinCiencias", max_length=50)
    fecha_Formacion = models.DateField("Fecha de Formación")
    lider = models.CharField("Lider", max_length=70)
    segundo_lider = models.CharField("Segundo Lider", max_length=70)
    grupLac = models.CharField("GrupLac", max_length=70)
    linea_investigacion = models.CharField("Linea de Investigación", max_length=70)

    class Meta:
        verbose_name = "Grupo de Investigación"
        verbose_name_plural = "Grupos de Investigaciones"

    def __str__(self):
        return self.nombre_Grupo




class compromiso(models.Model):
    codigo = models.CharField("Codigo", max_length=10, primary_key=True)
    tipo = models.CharField("Tipo", max_length=20)
    producto = models.CharField("Producto", max_length=50)
    cantidad = models.PositiveBigIntegerField("Cantidad")
    indicador = models.PositiveBigIntegerField("Indicador")
    medio_de_verificacion = models.CharField("Medio de Verificación", max_length=50)
    fecha = models.DateField()

    class Meta:
        verbose_name = "Compromiso"
        verbose_name_plural = "Compromisos"


class entidade(models.Model):
    nombre = models.CharField("Nombre", max_length=100)
    fecha_Manifestacion = models.DateField("Fecha Manifestación")
    numero_Contrato = models.IntegerField("Número Contrato")
    fecha_suscripcion = models.DateField("Fecha Suscripción")
    acta = models.CharField("Acta", max_length=200)

    class Meta:
        verbose_name = "Entidad"
        verbose_name_plural = "Entidades"




class proyecto_Innovacion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_proyecto = models.CharField("Titulo del Proyecto", max_length=250)
    palabras_claves = models.CharField("Palabras Claves", max_length=100)
    modalidad_presentacion1 = models.CharField("Modalidad 1", max_length=100)
    modalidad_presentacion2 = models.CharField("Modalidad 2", max_length=100)

    Lugar_Ejecucion = models.CharField("Lugar de Ejecución del Proyecto", max_length=50)

    facul = [
        ("CIENCIAS DE LA SALUD", "Ciencias de la Salud"),
        ("EDUCACIÓN", "Educación"),
        ("FACULTAD DE INGENIERIA", "Facultad de Ingenieria"),
        ("HUMANIDADES Y CIENCIAS SOCIALES", "Humanidades y Ciencias Sociales"),
        ("CCIENCIAS CONTABLES, ECONÓMIA", "Ciencias Contables, Económia")
    ]

    progra = [
        ("DERECHO", "Derecho"),
        ("TRABAJO SOCIAL", "Trabajo Social"),
        ("COMUNICACIÓN SOCIAL", "Comunicación Social"),
        ("PSICOLOGÍA", "Psicología"),
        ("MERCADEO", "Mercadeo"),
        ("CONTADURIA", "Contaduría Pública"),
        ("NEGOCIOS INTERNACIONALES", "Administración de Negocios Internacionales"),
        ("LICENCIATURA EN LITERATURA", "Licenciatura en Literatura"),
        ("LICENCIATURA EN MATEMATICÁS", "Licenciatura en Matemáticas"),
        ("LICENCIATURA EN EDUCACIÓN INFANTIL", "Licenciatura en Educación Infantil"),
        ("LICENCIATURA EN EDUCACIÓN BÁSICA PRIMARIA", "Licenciatura en Educación Básica Primaria"),
        ("ENFERMERÍA", "Enfermería"),
        ("TERAPIA OCUPACIONAL", "Terapia Ocupacional"),
        ("FISIOTERAPIA", "Fisioterapia"),
        ("NUTRICIÓN Y DIETÉTICA", "Nutrición y Dietética"),
        ("INGENIERÍA MECATRÓNICA", "Ingeniería Mecatrónica"),
        ("INGENIERÍA CIVIL", "Ingeniería Civil"),
        ("INGENIERÍA DE SISTEMAS", "Ingeniería de Sistemas"),
        ("INGENIERÍA AMBIENTAL", "Ingeniería Ambiental"),
        ("INGENIERÍA DE PROCESOS", "Ingeniería de Procesos"),
    ]

    facultad = models.CharField("Facultad", max_length=31, choices=facul, default="", blank=True)
    programa = models.CharField("Programa", max_length=41, choices=progra, default="INGENIERÍA DE SISTEMAS", blank=True)

    nombre_de_convocatoria = models.CharField("Nombre de Convocatoria", max_length=100, blank=True)
    fecha_Convocatoria = models.DateField("Fecha Convocatoria")


    #Tipo de Proyecto
    aplicada= models.BooleanField("Investigación Aplicada")
    tecnologico = models.BooleanField("Desarrollo Tecnológico")
    experimental = models.BooleanField("Desarrollo Experimental")
    innovacion = models.BooleanField("Innovación")
    #Ciencias Naturales
    matematicas = models.BooleanField("Matemáticas")
    quimica = models.BooleanField("Ciencias Químicas")
    computacion = models.BooleanField("Computación y Ciencias de la Información")
    tierra = models.BooleanField("Ciencias de la tierra y medioambientales")
    fisicas = models.BooleanField("Ciencias físicas")
    biologicas = models.BooleanField("Ciencias biológicas")
    otras_cien = models.BooleanField("Otras Ciencias Naturales")
    # Tecnologia
    Civil = models.BooleanField("Ingeniería Civil")
    mecanica = models.BooleanField("Ingeniería mecánica")
    quimica = models.BooleanField("Ingeniería química")
    electrica = models.BooleanField("Ingeniería eléctrica, electrónica e informática")
    medica = models.BooleanField("Ingeniería Médica")
    materiales = models.BooleanField("Ingeniería de materiales")
    ambiental = models.BooleanField("Ingeniería ambiental")
    biotecnologia_am = models.BooleanField("Biotecnología ambiental")
    industrial = models.BooleanField("Biotecnología industrial")
    Nanotecnologia = models.BooleanField("Nanotecnología")
    otras_inge = models.BooleanField("Otras Ingenierias")
    # ciencias medicas
    medicina_basica = models.BooleanField("Medicina básica")
    Medicina_clinica = models.BooleanField("Medicina clínica")
    cien_salud = models.BooleanField("Ciencias de la Salud")
    biotecnologia_salud = models.BooleanField("Biotecnología en salud")
    otras_cien = models.BooleanField("Otras Ciencias médicas")
    # ciencias agricolas
    agricultura = models.BooleanField("Agricultura, silvicultura y pesca")
    animales = models.BooleanField("Ciencias Animales y lechería")
    veterinarias = models.BooleanField("Ciencias Veterinarias")
    agricola = models.BooleanField("Biotecnología agrícola")
    otras_cien_agricolas = models.BooleanField("Otras Ciencias Agrícolas")
    #ciencias sociales
    Psicologia = models.BooleanField("Psicología")
    economia = models.BooleanField("Economía y negocios")
    educacion = models.BooleanField("Ciencias de la Educación")
    sociologia = models.BooleanField("Sociología")
    derecho = models.BooleanField("Derecho")
    cien_politicas = models.BooleanField("Ciencias Políticas")
    geografia_social = models.BooleanField("Geografía Social y Económica")
    periodismo = models.BooleanField("Periodismo y comunicaciones")
    otras_ciencias_sociales = models.BooleanField("Otras Ciencias Sociales")
    #humanidades
    historia = models.BooleanField("Historia y arqueología")
    idiomas = models.BooleanField("Idiomas y Literatura")
    otras_historias = models.BooleanField("Otras historias")
    Arte = models.BooleanField("Arte")
    otras_humanidades = models.BooleanField("Otras Humanidades")

    #1. Información general
    institucion_pertenece= models.CharField("Universidad o Institución a la que pertenece", max_length=100)
    grupo_de_Investigacion1 = models.ForeignKey( grupos_de_investigacion, related_name='Grupo', on_delete=models.CASCADE)
    director_grupo = models.CharField("Director (a) del Grupo de Investigación", max_length=50)
    grupLAC = models.CharField("Código GrupLAC", max_length=10)
    #reconocido minciencias
    si1 = models.BooleanField("Si")
    no1 = models.BooleanField("No")
    categoria= models.CharField("Categoria", max_length=50, blank=True)
    Linea_investigacion = models.CharField("Línea de investigación en la cual se vincula el proyecto", max_length=100, blank=True)
    desarrollo_sostenible = models.CharField("Objetivo del Desarrollo Sostenible ODS al cual se vincula el proyecto ", max_length=100, blank=True)
    mision_sabios = models.CharField("Foco Temático de la Misión de Sabios al cual se articula el proyecto", max_length=100, blank=True)

    # 2. Información general2
    institucion_pertenece2 = models.CharField("Universidad o Institución a la que pertenece", max_length=100)
    #grupo_de_Investigacion2 = models.ForeignKey(grupos_de_investigacion, related_name='Grupo Investigación ', on_delete=models.CASCADE)
    director_grupo2 = models.CharField("Director (a) del Grupo de Investigación", max_length=50)
    grupLAC2 = models.CharField("Código GrupLAC", max_length=10)
    # reconocido minciencias
    si12 = models.BooleanField("Si")
    no12 = models.BooleanField("No")
    categoria2 = models.CharField("Categoria", max_length=50, blank=True)
    Linea_investigacion2 = models.CharField("Línea de investigación en la cual se vincula el proyecto", max_length=100,blank=True)
    desarrollo_sostenible2 = models.CharField("Objetivo del Desarrollo Sostenible ODS al cual se vincula el proyecto ",max_length=100, blank=True)
    mision_sabios2 = models.CharField("Foco Temático de la Misión de Sabios al cual se articula el proyecto", max_length=100, blank=True)


    # -----------------------------------------------------------------------------------------------------------------------------------------



    objetivo_General = models.CharField("Objetivo General", max_length=300)
    objetivos_Especificos = models.CharField("Objetivos Especificos", max_length=300)
    tiempo_en_meses = models.PositiveIntegerField("Digite el Tiempo en Meses")
    fecha_de_Inicio = models.DateField("Fecha de Inicio")
    compromisos_obligatorios = models.ForeignKey(compromiso, related_name='Obligatorios', on_delete=models.CASCADE)
    participantes_Universidad_Mariana = models.CharField("Nombres de los Participantes que pertenezcan Universidad Mariana", max_length=200, blank=True)
    participantes_Proyecto = models.CharField("Participantes del Proyecto",max_length=300)
    financiacion_por_Entidad = models.BooleanField("Financiación por Entidad", default=True, blank=True)
    porcentaje_Total = models.PositiveIntegerField("Porcentaje Total")
    Rec_Frescos = models.PositiveIntegerField("Rec Frescos")
    Rec_Especie = models.CharField("Rec Especie", max_length=200, blank=True)
    ejecucion_por_Anio = models.CharField("Ejecución por Año", max_length=100, blank=True)
    Financiacion_por_Direccion_de_Investigaciones = models.BooleanField("Financiación por Dirección de Investigaciones", default=True, blank=True)
    centro_de_Costos = models.CharField("Centro de Costos", max_length=100, blank=True)
    ejecucion_por_Anio2 = models.CharField("Ejecución por Año", max_length=50, blank=True)
    entidades_Participantes = models.ForeignKey(entidade, on_delete=models.CASCADE)
    propiedad_intelectual = models.CharField("Propiedad Intelectual", max_length=300, blank=True)
    total_de_Propiedad_Intelectual = models.IntegerField("Total de propiedad Intelectual")
    funciones_de_Estudiantes_en_Formacion = models.BooleanField("Funciones de Estudiantes en Formación", default=True, blank=True)

    formacion = [
        ("PREGRADO", "Pregrado"),
        ("POSGRADO", "Posgrado")
    ]
    estudiante = models.CharField("Estudiante", max_length=8, choices=formacion, default="PREGRADO", blank=True)

    codigo_de_etica_institucional = models.CharField("Codigo de etica Institucional", max_length=300, blank=True)
    acuerdo_confidencialidad = models.CharField("Acuerdo Confidencial", max_length=400, blank=True)
    compromisos_de_los_Investigadores = models.CharField("Compromisos de los Investigadores", max_length=400, blank=True)
    constancia = models.CharField("Constancia", max_length=400, blank=True)
    modificaciones = models.CharField("Modificaciones", max_length=400, blank=True)
    firmas = models.CharField("Firmas", max_length=200, blank=True)
    responsables = models.CharField("Responsables", max_length=300, blank=True)


    class Meta:
        verbose_name = "Proyecto de Innovación"
        verbose_name_plural = "Proyectos de Innovación"



class proyecto_Tecnologico(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_proyecto = models.CharField("Titulo del Proyecto", max_length=250)
    palabras_claves = models.CharField("Palabras Claves", max_length=100)
    nombre_de_convocatoria = models.CharField("Nombre de Convocatoria", max_length=100, blank=True)
    tiempo_en_meses = models.PositiveIntegerField("Digite el Tiempo en Meses")
    Lugar_Ejecucion = models.CharField("Lugar de Ejecución del Proyecto", max_length=50)

    #------------ foco o reto atendido----------------------------------------------------------------------------------

    #------------foco---------------

    tecnologia_convergentes_e_industrias = models.BooleanField("Tecnología convergentes e industrias 4.0", blank=True, null=True)
    biotecnologia_bioeconomia_economia = models.BooleanField("Biotecnología, bioeconomía, economía creativa y medio ambiente", blank=True, null=True)
    industrias_creativas_culturales = models.BooleanField("Industrias creativas y culturales y patrimonio cultural", blank=True, null=True)
    energias_sostenibles_economia_circular = models.BooleanField("Energías sostenibles, economía circular y cambio climático", blank=True, null=True)
    innovacion_salud_bienestar = models.BooleanField("Innovación en salud y bienestar", blank=True, null=True)
    conocimiento_educacion_para_inclusion = models.BooleanField("Conocimiento y educación para la inclusión social y el desarrollo de habilidades socioemocionales", blank=True, null=True)

    # ------------Retos---------------

    promocion_de_productividad = models.BooleanField("Promoción de la productividad y optimización del cultivo de cacao.", blank=True, null=True)
    automatizacion_de_produccion = models.BooleanField("Automatización de la producción para suplir la escasa mano de obra.", blank=True, null=True)
    diversificacion_en_presentaciones = models.BooleanField("Diversificación en las presentaciones comerciales de la panela.", blank=True, null=True)
    pulverizadora_de_leche_polvo = models.BooleanField("Pulverizadora de leche en polvo para la optimización del mercado de leche", blank=True, null=True)
    factibilidad_de_planta_concentrados = models.BooleanField("Factibilidad de una planta de concentrados para bovinos de leche, o maquila de concentrados.", blank=True, null=True)
    mejoramiento_estatus_sanitario_bovino = models.BooleanField("Mejoramiento del estatus sanitario bovino y buenas prácticas ganaderas.", blank=True, null=True)
    erradicacion_disminucion_de_punta_morada = models.BooleanField("Erradicación o disminución de la punta morada de los cultivos de papa en los suelos.", blank=True, null=True)
    disminucion_de_costos = models.BooleanField("Disminución de costos de producción de papa.", null=True)

    # ------------Lider---------------

    txt_nombre_InvestigadorP = models.CharField("Investigador principal o líder del proyecto", max_length=200)
    txt_documentoIdentidad_InvestigadorP = models.CharField("Documento de identidad investigador principal", max_length=20)
    txt_grupoInvestigacion_InvestigadorP = models.CharField("Grupo de Investigación", max_length=300)
    txt_nivelEstudio_investigadorP = models.CharField("Nivel de estudio", max_length=300)
    txt_institucionVinculado_InvestigadorP = models.CharField("Institución a la que se encuetra vinculado", max_length=300)
    txt_funciones_InvestigadorP = models.CharField("Funciones del investigador principal", max_length=400)
    txt_dedicacionSemanal_InvestigadorP = models.CharField("Dedicacion semanal investigador principal", max_length=100)

    # ------------Investigador-Interno---------------

    txt_nombre_InvestigadorInterno = models.CharField("Nombre investigador Interno", max_length=200, blank=True, null=True)
    txt_documentoIdentidad_InvestigadorInterno = models.CharField("Documento investigador Interno", max_length=20, blank=True, null=True)
    txt_grupoInvestigacion_InvestigadorInterno = models.CharField("Grupo de Investigación", max_length=300, blank=True, null=True)
    txt_nivelEstudio_investigadorInterno = models.CharField("Nivel de estudio investigador Interno", max_length=300, blank=True, null=True)
    txt_institucionVinculado_InvestigadorInterno =  models.CharField("Institución a la que se encuetra vinculado", max_length=300, blank=True, null=True)
    txt_funciones_InvestigadorInterno = models.CharField("Funciones del investigador Interno", max_length=400, blank=True, null=True)
    txt_dedicacionSemanal_InvestigadorInterno = models.CharField("Dedicacion semanal investigador interno", max_length=100, blank=True, null=True)



    # ------------Investigador-Externo---------------

    txt_nombre_InvestigadorExterno = models.CharField("Nombre investigador externo", max_length=200, blank=True, null=True)
    txt_documentoIdentidad_InvestigadorExterno = models.CharField("Documento investigador Externo", max_length=20, blank=True, null=True)
    txt_grupoInvestigacion_InvestigadorExterno = models.CharField("Grupo de Investigación de investigador externo", max_length=300, blank=True, null=True)
    txt_nivelEstudio_investigadorExterno = models.CharField("Nivel de estudio investigador Externo", max_length=300, blank=True, null=True)
    txt_institucionVinculado_InvestigadorExterno = models.CharField("Institución a la que se encuetra vinculado", max_length=300, blank=True, null=True)
    txt_funciones_InvestigadorExterno = models.CharField("Funciones del investigador Externo", max_length=400, blank=True, null=True)
    txt_dedicacionSemanal_InvestigadorExterno = models.CharField("Dedicacion semanal investigador Externo", max_length=100, blank=True, null=True)


    # ------------Semillerista investigador principal---------------

    txt_nombre_Auxiliar_Interno1 = models.CharField("Nombre semillerista - investigador principal", max_length=200, blank=True, null=True)
    txt_documentoIdentidad_Auxliar_Interno1 = models.CharField("Documento semillerista - investigador principal", max_length=20, blank=True, null=True)
    txt_codigoEstudiantil = models.CharField("Codigo Estudiantil", max_length=20, blank=True, null=True)
    txt_institucionVinculado_Auxliar_Interno1 = models.CharField("Institución a la que se encuetra vinculado", max_length=300, blank=True, null=True)
    txt_funciones_Auxliar_Interno1 = models.CharField("Funciones del semillerista - investigador principal", max_length=400, blank=True, null=True)
    txt_dedicacionSemanal_Auxliar_Interno1 = models.CharField("Dedicacion semanal semillerista - investigador principal", max_length=100, blank=True, null=True)


    # ------------Co investigador---------------
    txt_nombre_Auxiliar_externo = models.CharField("Nombre Coinvestigador", max_length=200, blank=True, null=True)
    txt_documentoIdentidad_Auxiliar_externo = models.CharField("Documento Coinvestigador", max_length=20, blank=True, null=True)
    txt_codigoEstudiantil_Coinvestigador = models.CharField("Codigo Estudiantil Coinvestigador", max_length=20, blank=True, null=True)
    txt_institucionVinculado_Auxiliar_externo = models.CharField("Institución a la que se encuetra vinculado Coinvestigador", max_length=300, blank=True, null=True)
    txt_funciones_Auxiliar_externo = models.CharField("Funciones del semillerista Coinvestigador", max_length=400, blank=True, null=True)
    txt_dedicacionSemanal_Auxiliar_externo = models.CharField("Dedicacion semanal Coinvestigador", max_length=100, blank=True, null=True)



    # ------------Resumen y objetivos---------------

    txt_4resumen_ejecutivo = models.TextField("Resumen Ejecutivo", max_length=3000, blank=True, null=True)
    txt_5objetivos = models.TextField("Objetivo General y Especificos", max_length=1000, blank=True, null=True)
    txt_6descripcion = models.TextField("Descripción del problema", max_length=3000, blank=True, null=True)
    txt_7justificacion = models.TextField("Estado de la tecnica", max_length=3000, blank=True, null=True)
    txt_8marcoConceptual = models.TextField("Marco conceptual", max_length=5000, blank=True, null=True)
    txt_8antecedentes = models.TextField("Justificación del nivel de TRL", max_length=5000, blank=True, null=True)
    txt_10novedadProyecto = models.TextField("Justificación del carácter inventivo", max_length=5000, blank=True, null=True)
    txt_11metodologia = models.TextField("Metodologia", max_length=5000, blank=True, null=True)
    txt_14componente_etico = models.TextField("Licencias ambientales", max_length=5000, blank=True, null=True)
    txt_15identidad = models.TextField("Riesgos Posibles", max_length=5000, blank=True, null=True)
    txt_17alineacion = models.TextField("Alineación con políticas nacionales", max_length=5000, blank=True, null=True)
    text_presupuesto = models.TextField("Presupuesto", max_length=5000, blank=True, null=True)




    # ------------Cronograma---------------

    txt_actividad1_Objetivo1 = models.TextField("Actividad de objetivo 1", max_length=1000, blank=True, null=True)
    txt_producto1_Objetivo1 = models.TextField("Producto de objetivo 1", max_length=1000, blank=True, null=True)
    txt_mes1_Objetivo1 = models.TextField("Mes de objetivo 1", max_length=100, blank=True, null=True)
    txt_actividad2_Objetivo1 = models.TextField("Actividad 2 de objetivo 1", max_length=1000, blank=True, null=True)
    txt_producto2_Objetivo1 = models.TextField("Producto 2 de objetivo 1", max_length=1000, blank=True, null=True)
    txt_mes2_Objetivo1 = models.TextField("Mes 2 de objetivo 1", max_length=100, blank=True, null=True)
    txt_actividad3_Objetivo1 = models.TextField("Actividad 3 de objetivo 1", max_length=1000, blank=True, null=True)
    txt_producto3_Objetivo1 = models.TextField("Producto 3 de objetivo 1", max_length=1000, blank=True, null=True)
    txt_mes3_Objetivo1 = models.TextField("Mes 3 de objetivo 1", max_length=100, blank=True, null=True)

    txt_actividad1_Objetivo2 = models.TextField("Actividad de objetivo 2", max_length=1000, blank=True, null=True)
    txt_producto1_Objetivo2 = models.TextField("Producto de objetivo 2", max_length=1000, blank=True, null=True)
    txt_mes1_Objetivo2 = models.TextField("Mes de objetivo 2", max_length=100, blank=True, null=True)
    txt_actividad2_Objetivo2 = models.TextField("Actividad 2 de objetivo 2", max_length=1000, blank=True, null=True)
    txt_producto2_Objetivo2 = models.TextField("Producto 2 de objetivo 2", max_length=1000, blank=True, null=True)
    txt_mes2_Objetivo2 = models.TextField("Mes 2 de objetivo 2", max_length=100, blank=True, null=True)
    txt_actividad3_Objetivo2 = models.TextField("Actividad 3 de objetivo 2", max_length=1000, blank=True, null=True)
    txt_producto3_Objetivo2 = models.TextField("Producto 3 de objetivo 2", max_length=1000, blank=True, null=True)
    txt_mes3_Objetivo2 = models.TextField("Mes 3 de objetivo 2", max_length=100, blank=True, null=True)

    txt_entregainformeavance = models.TextField("Informe de avance", max_length=100, blank=True, null=True)

    txt_actividad1_Objetivo3 = models.TextField("Actividad de objetivo 3", max_length=1000, blank=True, null=True)
    txt_producto1_Objetivo3 = models.TextField("Producto de objetivo 3", max_length=1000, blank=True, null=True)
    txt_mes1_Objetivo3 = models.TextField("Mes de objetivo 3", max_length=100, blank=True, null=True)
    txt_actividad2_Objetivo3 = models.TextField("Actividad 2 de objetivo 3", max_length=1000, blank=True, null=True)
    txt_producto2_Objetivo3 = models.TextField("Producto 2 de objetivo 3", max_length=1000, blank=True, null=True)
    txt_mes2_Objetivo3 = models.TextField("Mes 2 de objetivo 3", max_length=100, blank=True, null=True)
    txt_actividad3_Objetivo3 = models.TextField("Actividad 3 de objetivo 3", max_length=1000, blank=True, null=True)
    txt_producto3_Objetivo3 = models.TextField("Producto 3 de objetivo 3", max_length=1000, blank=True, null=True)
    txt_mes3_Objetivo3 = models.TextField("Mes 3 de objetivo 3", max_length=100, blank=True, null=True)
    txt_actividad4_Objetivo3 = models.TextField("Actividad 4 de objetivo 3", max_length=1000, blank=True, null=True)
    txt_producto4_Objetivo3 = models.TextField("Producto 4 de objetivo 3", max_length=1000, blank=True, null=True)
    txt_mes4_Objetivo3 = models.TextField("Mes 4 de objetivo 3", max_length=100, blank=True, null=True)

    txt_productos_Estrategiadivulgacion = models.TextField("Estrategia de divulgación", max_length=1000, blank=True, null=True)
    txt_entregainformafinal = models.TextField("Informe final", max_length=5000, blank=True, null=True)
    txt_referecias = models.TextField("Referecias", max_length=5000, blank=True, null=True)



    # ------------Impacto esperado---------------

    txt_campoAcademico_Indicador = models.TextField("Indicador Academico", max_length=1000, blank=True, null=True)
    txt_desarrolloTecnologico_Indicador = models.TextField("Indicador Tecnologico", max_length=1000, blank=True, null=True)
    txt_social_Indicador = models.TextField("Indicador Social", max_length=1000, blank=True, null=True)
    txt_educativo_Indicador = models.TextField("Indicador Educativo", max_length=1000, blank=True, null=True)
    txt_simbolico_Indicador = models.TextField("Indicador Simbolico", max_length=1000, blank=True, null=True)
    txt_economicos_Indicador = models.TextField("Indicador Economico", max_length=1000, blank=True, null=True)

    facul = [
        ("CIENCIAS DE LA SALUD", "Ciencias de la Salud"),
        ("EDUCACIÓN", "Educación"),
        ("FACULTAD DE INGENIERIA", "Facultad de Ingenieria"),
        ("HUMANIDADES Y CIENCIAS SOCIALES", "Humanidades y Ciencias Sociales"),
        ("CCIENCIAS CONTABLES, ECONÓMIA", "Ciencias Contables, Económia")
    ]

    progra = [
        ("DERECHO", "Derecho"),
        ("TRABAJO SOCIAL", "Trabajo Social"),
        ("COMUNICACIÓN SOCIAL", "Comunicación Social"),
        ("PSICOLOGÍA", "Psicología"),
        ("MERCADEO", "Mercadeo"),
        ("CONTADURIA", "Contaduría Pública"),
        ("NEGOCIOS INTERNACIONALES", "Administración de Negocios Internacionales"),
        ("LICENCIATURA EN LITERATURA", "Licenciatura en Literatura"),
        ("LICENCIATURA EN MATEMATICÁS", "Licenciatura en Matemáticas"),
        ("LICENCIATURA EN EDUCACIÓN INFANTIL", "Licenciatura en Educación Infantil"),
        ("LICENCIATURA EN EDUCACIÓN BÁSICA PRIMARIA", "Licenciatura en Educación Básica Primaria"),
        ("ENFERMERÍA", "Enfermería"),
        ("TERAPIA OCUPACIONAL", "Terapia Ocupacional"),
        ("FISIOTERAPIA", "Fisioterapia"),
        ("NUTRICIÓN Y DIETÉTICA", "Nutrición y Dietética"),
        ("INGENIERÍA MECATRÓNICA", "Ingeniería Mecatrónica"),
        ("INGENIERÍA CIVIL", "Ingeniería Civil"),
        ("INGENIERÍA DE SISTEMAS", "Ingeniería de Sistemas"),
        ("INGENIERÍA AMBIENTAL", "Ingeniería Ambiental"),
        ("INGENIERÍA DE PROCESOS", "Ingeniería de Procesos"),
    ]

    facultad = models.CharField("Facultad", max_length=31, choices=facul, default="", blank=True)
    programa = models.CharField("Programa", max_length=41, choices=progra, default="INGENIERÍA DE SISTEMAS", blank=True)





    class Meta:
        verbose_name = "Proyecto de Desarrollo Tecnologico"
        verbose_name_plural = "Proyectos de Desarrollo Tecnologico"



class proyecto_Cientifico(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_proyecto = models.CharField("Titulo del Proyecto", max_length=250)
    palabras_claves = models.CharField("Palabras Claves", max_length=100)
    modalidad_presentacion1 = models.CharField("Modalidad 1", max_length=100)
    modalidad_presentacion2 = models.CharField("Modalidad 2", max_length=100)

    Lugar_Ejecucion = models.CharField("Lugar de Ejecución del Proyecto", max_length=50)

    facul = [
        ("CIENCIAS DE LA SALUD", "Ciencias de la Salud"),
        ("EDUCACIÓN", "Educación"),
        ("FACULTAD DE INGENIERIA", "Facultad de Ingenieria"),
        ("HUMANIDADES Y CIENCIAS SOCIALES", "Humanidades y Ciencias Sociales"),
        ("CCIENCIAS CONTABLES, ECONÓMIA", "Ciencias Contables, Económia")
    ]

    progra = [
        ("DERECHO", "Derecho"),
        ("TRABAJO SOCIAL", "Trabajo Social"),
        ("COMUNICACIÓN SOCIAL", "Comunicación Social"),
        ("PSICOLOGÍA", "Psicología"),
        ("MERCADEO", "Mercadeo"),
        ("CONTADURIA", "Contaduría Pública"),
        ("NEGOCIOS INTERNACIONALES", "Administración de Negocios Internacionales"),
        ("LICENCIATURA EN LITERATURA", "Licenciatura en Literatura"),
        ("LICENCIATURA EN MATEMATICÁS", "Licenciatura en Matemáticas"),
        ("LICENCIATURA EN EDUCACIÓN INFANTIL", "Licenciatura en Educación Infantil"),
        ("LICENCIATURA EN EDUCACIÓN BÁSICA PRIMARIA", "Licenciatura en Educación Básica Primaria"),
        ("ENFERMERÍA", "Enfermería"),
        ("TERAPIA OCUPACIONAL", "Terapia Ocupacional"),
        ("FISIOTERAPIA", "Fisioterapia"),
        ("NUTRICIÓN Y DIETÉTICA", "Nutrición y Dietética"),
        ("INGENIERÍA MECATRÓNICA", "Ingeniería Mecatrónica"),
        ("INGENIERÍA CIVIL", "Ingeniería Civil"),
        ("INGENIERÍA DE SISTEMAS", "Ingeniería de Sistemas"),
        ("INGENIERÍA AMBIENTAL", "Ingeniería Ambiental"),
        ("INGENIERÍA DE PROCESOS", "Ingeniería de Procesos"),
    ]

    facultad = models.CharField("Facultad", max_length=31, choices=facul, default="", blank=True)
    programa = models.CharField("Programa", max_length=41, choices=progra, default="INGENIERÍA DE SISTEMAS", blank=True)

    nombre_de_convocatoria = models.CharField("Nombre de Convocatoria", max_length=100, blank=True)
    fecha_Convocatoria = models.DateField("Fecha Convocatoria")


    #Tipo de Proyecto
    aplicada= models.BooleanField("Investigación Aplicada")
    tecnologico = models.BooleanField("Desarrollo Tecnológico")
    experimental = models.BooleanField("Desarrollo Experimental")
    innovacion = models.BooleanField("Innovación")
    #Ciencias Naturales
    matematicas = models.BooleanField("Matemáticas")
    quimica = models.BooleanField("Ciencias Químicas")
    computacion = models.BooleanField("Computación y Ciencias de la Información")
    tierra = models.BooleanField("Ciencias de la tierra y medioambientales")
    fisicas = models.BooleanField("Ciencias físicas")
    biologicas = models.BooleanField("Ciencias biológicas")
    otras_cien = models.BooleanField("Otras Ciencias Naturales")
    # Tecnologia
    Civil = models.BooleanField("Ingeniería Civil")
    mecanica = models.BooleanField("Ingeniería mecánica")
    quimica = models.BooleanField("Ingeniería química")
    electrica = models.BooleanField("Ingeniería eléctrica, electrónica e informática")
    medica = models.BooleanField("Ingeniería Médica")
    materiales = models.BooleanField("Ingeniería de materiales")
    ambiental = models.BooleanField("Ingeniería ambiental")
    biotecnologia_am = models.BooleanField("Biotecnología ambiental")
    industrial = models.BooleanField("Biotecnología industrial")
    Nanotecnologia = models.BooleanField("Nanotecnología")
    otras_inge = models.BooleanField("Otras Ingenierias")
    # ciencias medicas
    medicina_basica = models.BooleanField("Medicina básica")
    Medicina_clinica = models.BooleanField("Medicina clínica")
    cien_salud = models.BooleanField("Ciencias de la Salud")
    biotecnologia_salud = models.BooleanField("Biotecnología en salud")
    otras_cien = models.BooleanField("Otras Ciencias médicas")
    # ciencias agricolas
    agricultura = models.BooleanField("Agricultura, silvicultura y pesca")
    animales = models.BooleanField("Ciencias Animales y lechería")
    veterinarias = models.BooleanField("Ciencias Veterinarias")
    agricola = models.BooleanField("Biotecnología agrícola")
    otras_cien_agricolas = models.BooleanField("Otras Ciencias Agrícolas")
    #ciencias sociales
    Psicologia = models.BooleanField("Psicología")
    economia = models.BooleanField("Economía y negocios")
    educacion = models.BooleanField("Ciencias de la Educación")
    sociologia = models.BooleanField("Sociología")
    derecho = models.BooleanField("Derecho")
    cien_politicas = models.BooleanField("Ciencias Políticas")
    geografia_social = models.BooleanField("Geografía Social y Económica")
    periodismo = models.BooleanField("Periodismo y comunicaciones")
    otras_ciencias_sociales = models.BooleanField("Otras Ciencias Sociales")
    #humanidades
    historia = models.BooleanField("Historia y arqueología")
    idiomas = models.BooleanField("Idiomas y Literatura")
    otras_historias = models.BooleanField("Otras historias")
    Arte = models.BooleanField("Arte")
    otras_humanidades = models.BooleanField("Otras Humanidades")

    #1. Información general
    institucion_pertenece= models.CharField("Universidad o Institución a la que pertenece", max_length=100)
    #grupo_de_Investigacion1 = models.ForeignKey( grupos_de_investigacion, related_name='Grupo Investigación ', on_delete=models.CASCADE)
    director_grupo = models.CharField("Director (a) del Grupo de Investigación", max_length=50)
    grupLAC = models.CharField("Código GrupLAC", max_length=10)
    #reconocido minciencias
    si1 = models.BooleanField("Si")
    no1 = models.BooleanField("No")
    categoria= models.CharField("Categoria", max_length=50, blank=True)
    Linea_investigacion = models.CharField("Línea de investigación en la cual se vincula el proyecto", max_length=100, blank=True)
    desarrollo_sostenible = models.CharField("Objetivo del Desarrollo Sostenible ODS al cual se vincula el proyecto ", max_length=100, blank=True)
    mision_sabios = models.CharField("Foco Temático de la Misión de Sabios al cual se articula el proyecto", max_length=100, blank=True)

    # 2. Información general2
    institucion_pertenece2 = models.CharField("Universidad o Institución a la que pertenece", max_length=100)
    #grupo_de_Investigacion2 = models.ForeignKey(grupos_de_investigacion, related_name='Grupo Investigación ', on_delete=models.CASCADE)
    director_grupo2 = models.CharField("Director (a) del Grupo de Investigación", max_length=50)
    grupLAC2 = models.CharField("Código GrupLAC", max_length=10)
    # reconocido minciencias
    si12 = models.BooleanField("Si")
    no12 = models.BooleanField("No")
    categoria2 = models.CharField("Categoria", max_length=50, blank=True)
    Linea_investigacion2 = models.CharField("Línea de investigación en la cual se vincula el proyecto", max_length=100,blank=True)
    desarrollo_sostenible2 = models.CharField("Objetivo del Desarrollo Sostenible ODS al cual se vincula el proyecto ",max_length=100, blank=True)
    mision_sabios2 = models.CharField("Foco Temático de la Misión de Sabios al cual se articula el proyecto", max_length=100, blank=True)


    # -----------------------------------------------------------------------------------------------------------------------------------------



    objetivo_General = models.CharField("Objetivo General", max_length=300)
    objetivos_Especificos = models.CharField("Objetivos Especificos", max_length=300)
    tiempo_en_meses = models.PositiveIntegerField("Digite el Tiempo en Meses")
    fecha_de_Inicio = models.DateField("Fecha de Inicio")
    #compromisos_obligatorios = models.ForeignKey(compromiso, related_name='compromisos_Obligatorios', on_delete=models.CASCADE)
    participantes_Universidad_Mariana = models.CharField("Nombres de los Participantes que pertenezcan Universidad Mariana", max_length=200, blank=True)
    participantes_Proyecto = models.CharField("Participantes del Proyecto",max_length=300)
    financiacion_por_Entidad = models.BooleanField("Financiación por Entidad", default=True, blank=True)
    porcentaje_Total = models.PositiveIntegerField("Porcentaje Total")
    Rec_Frescos = models.PositiveIntegerField("Rec Frescos")
    Rec_Especie = models.CharField("Rec Especie", max_length=200, blank=True)
    ejecucion_por_Anio = models.CharField("Ejecución por Año", max_length=100, blank=True)
    Financiacion_por_Direccion_de_Investigaciones = models.BooleanField("Financiación por Dirección de Investigaciones", default=True, blank=True)
    centro_de_Costos = models.CharField("Centro de Costos", max_length=100, blank=True)
    ejecucion_por_Anio2 = models.CharField("Ejecución por Año", max_length=50, blank=True)
    entidades_Participantes = models.ForeignKey( entidade, on_delete=models.CASCADE)
    propiedad_intelectual = models.CharField("Propiedad Intelectual", max_length=300, blank=True)
    total_de_Propiedad_Intelectual = models.IntegerField("Total de propiedad Intelectual")
    funciones_de_Estudiantes_en_Formacion = models.BooleanField("Funciones de Estudiantes en Formación", default=True, blank=True)

    formacion = [
        ("PREGRADO", "Pregrado"),
        ("POSGRADO", "Posgrado")
    ]
    estudiante = models.CharField("Estudiante", max_length=8, choices=formacion, default="PREGRADO", blank=True)

    codigo_de_etica_institucional = models.CharField("Codigo de etica Institucional", max_length=300, blank=True)
    acuerdo_confidencialidad = models.CharField("Acuerdo Confidencial", max_length=400, blank=True)
    compromisos_de_los_Investigadores = models.CharField("Compromisos de los Investigadores", max_length=400, blank=True)
    constancia = models.CharField("Constancia", max_length=400, blank=True)
    modificaciones = models.CharField("Modificaciones", max_length=400, blank=True)
    firmas = models.CharField("Firmas", max_length=200, blank=True)
    responsables = models.CharField("Responsables", max_length=300, blank=True)


    class Meta:
        verbose_name = "Proyecto de Investigación Cientifica"
        verbose_name_plural = "Proyectos de Investigación Cientifica"





class investigadores(models.Model):

    id = models.AutoField( primary_key=True)
    nombres_completos = models.CharField("Nombres Completos", max_length=100)
    cedula = models.CharField("Cedula", max_length=10)

    # creo lista
    sexos = [
        ("FEMENINO", "Femenino"),
        ("MASCULINO", "Masculino")
    ]
    sexo = models.CharField("Sexo", max_length=9, choices=sexos, default="MASCULINO")

    grupo_de_Investigación = models.ForeignKey(grupos_de_investigacion, related_name='grupo_al_que_pertenece', on_delete=models.CASCADE)
    categoria_Grupo = models.CharField("Categoria Grupo", max_length=1, blank=True)
    codigo_Grupo = models.CharField("Código Grupo", max_length=10)

    # creo lista
    facultad = [
        ("CIENCIAS DE LA SALUD", "Ciencias de la Salud"),
        ("EDUCACIÓN", "Educación"),
        ("FACULTAD DE INGENIERIA", "Facultad de Ingenieria"),
        ("HUMANIDADES Y CIENCIAS SOCIALES", "Humanidades y Ciencias Sociales"),
        ("CCIENCIAS CONTABLES, ECONÓMIA", "Ciencias Contables, Económia")
    ]

    facultad_adscrito = models.CharField("Facultad Adscrito", max_length=31, choices=facultad, default="")

    tipo_de_Contrato = models.CharField("Tipo de Contrato", max_length=40)
    vinculacion = models.CharField("Viculación", max_length=40)
    horas_de_Contratacion = models.PositiveIntegerField("Horas de Contratación")
    anio_de_vinculacion_al_Grupo = models.PositiveBigIntegerField("Año de vinculación al Grupo")
    anio_retiro = models.PositiveBigIntegerField("Año Retiro")
    categoria_Escalafon = models.CharField("Categoria Escalafón", max_length=20)
    Categoria_Investigador_convoctoria = models.CharField("Categoria Investigador Convocatoria", max_length=20, blank=True)
    formacion = models.CharField("Formación", max_length=20)

    gmail = models.CharField("Gmail", max_length=40, blank=True)
    contrasenia = models.CharField("Contraseña", max_length=30)
    CvLac = models.CharField("CvLac", max_length=200, blank=True)
    estudios_Pregrado = models.CharField("Estudios Pregrado", max_length=200, blank=True)
    estudios_Posgrado = models.CharField("Estudias Postgrado", max_length=200, blank=True)

    estado = models.BooleanField("Estado", default=True, blank=True)
    #productos = models.ForeignKey(producto, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Investigador"
        verbose_name_plural = "Investigadores"





