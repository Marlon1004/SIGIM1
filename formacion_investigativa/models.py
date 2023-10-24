from django.db import models
from investigadores.models import grupos_de_investigacion, investigadores, proyecto_Innovacion

# Create your models here.


class eventos_Relacionados(models.Model):
    id = models.AutoField(primary_key=True)
    eventos_Nacionales=models.CharField("Eventos Nacionales", max_length=1000)
    eventos_Internacionales = models.CharField("Eventos Internacionales", max_length=1000)
    reconocimientos= models.CharField("Reconocimientos", max_length=1000, blank=True)
    vinculados_inveProfesorales = models.CharField("Vinculados InveProfesorales", max_length=1000)
    Grupo_de_Investigación = models.ForeignKey( grupos_de_investigacion, null=False, on_delete=models.CASCADE)
   
    
    class Meta:
        verbose_name = "Evento Relacionado"
        verbose_name_plural = "Eventos Relacionados"




class proyecto_semillerista(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_Proyecto=models.PositiveIntegerField("Codigo Proyecto")
    Nombre_del_Proyecto=models.CharField("Nombre del Proyecto", max_length=200)

    estado_del_Proyecto=models.CharField("Estado del Proyecto", max_length=100)
    linea_de_Investigacion=models.CharField("Linea de Investigación", max_length=100)
    convalidado=models.BooleanField("Convalidado", default=True)

    class Meta:
        verbose_name = "Proyecto Semillerista"
        verbose_name_plural = "Proyectos Semilleristas"

    def __str__(self):
        return self.Nombre_del_Proyecto


class semillerista(models.Model):

    id = models.AutoField(primary_key=True)
    cedula=models.PositiveIntegerField("Cedula")
    semillero=models.CharField("Semillero", max_length=30)
    codigo_Proyecto=models.PositiveIntegerField("Codigo del Proyecto")
    fecha_Vinculacion=models.DateField("Fecha Vonculación")
    nombre_Completo=models.CharField("Nombre Completo", max_length=50)
    codigo_Estudiantil=models.IntegerField("Codigo Estudiantil")

    # creo lista
    facultad = [
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

    facultad_adscrito=models.CharField("Facultad Adscrito", max_length=31, choices=facultad, default="I")
    programa=models.CharField("Programa", max_length=41, choices=progra, null=True, blank=True)
    semestre=models.PositiveIntegerField("Semestre", blank=True)
    correo=models.EmailField("Correo", blank=True)
    telefono=models.IntegerField("Telefono", blank=True)
    eventos_Relacionados=models.ForeignKey( eventos_Relacionados, null=False, on_delete=models.CASCADE)
    financiacion_interna=models.PositiveIntegerField("Financiación Interna")
    financiacion_externa = models.PositiveIntegerField("Financiación Externa", blank=True)
    proyectos_Vinculados= models.ForeignKey( proyecto_semillerista, null=False, on_delete=models.CASCADE)
    relaciones_Politicas_Internacionales=models.CharField("Relaciones Politicas Internacionales", max_length=200)
    Describir_Tema=models.CharField("Describir Tema", max_length=150)
    reto=models.CharField("Reto", max_length=150)

    

    class Meta:
        verbose_name = "Semillerista"
        verbose_name_plural = "Semilleristas"

    def __str__(self):
        return self.nombre_Completo


class semillero(models.Model):

    id = models.AutoField(primary_key=True)
    nombre=models.CharField("Nombre", max_length=200)
    coordinador = models.CharField("Coordinador", max_length=100)
    integrantes_Activos=models.ForeignKey(semillerista, related_name='integrantes_semilleristas', null=False, on_delete=models.CASCADE)
    facul= [
        ("CIENCIAS DE LA SALUD", "Ciencias de la Salud"),
        ("EDUCACIÓN", "Educación"),
        ("FACULTAD DE INGENIERIA", "Facultad de Ingenieria"),
        ("HUMANIDADES Y CIENCIAS SOCIALES", "Humanidades y Ciencias Sociales"),
        ("CCIENCIAS CONTABLES, ECONÓMIA", "Ciencias Contables, Económia")
    ]
    facultad = models.CharField("Facultad", max_length=31, choices=facul, default="")
    programa = models.CharField("Programa", max_length=50, blank=True)
    lider_Semillero = models.CharField("Lider Semillero", max_length=50)
    fecha_de_Creacion = models.DateField("Fecha de Creación")
    linea_Investigacion = models.CharField("Linea de Investigación", max_length=100)
    logo = models.ImageField(blank=True)

    class Meta:
        verbose_name = "Semillero"
        verbose_name_plural = "Semilleros"

    def __str__(self):
        return self.nombre


class coInvestigadores(models.Model):

    id = models.AutoField(primary_key=True)
    nombre=models.CharField("Nombre", max_length=50)
    Grupo_de_Investigación_al_que_Pertenece=models.ForeignKey(grupos_de_investigacion, null=False, on_delete=models.CASCADE)
    proyecto_de_investigacion = models.CharField("Proyecto de Investigación", max_length=200)

    investigadores_vinculados= models.ForeignKey(investigadores, null=True, on_delete=models.CASCADE)

    anio_vinculacion=models.PositiveIntegerField("Año Vinculación")
    nombre_Asesor=models.CharField("Nombre del Asesor", max_length=50)

    programa = [
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

    programa_academico=models.CharField("Programa Académico", max_length=41, choices=programa, default="INGENIERÍA DE SISTEMAS", null=True, blank=True)
    correo=models.EmailField("Correo", blank=True)
    telefono=models.PositiveIntegerField("Teléfono", blank=True)

    class Meta:
        verbose_name = "CoInvestigador"
        verbose_name_plural = "CoInvestigadores"
    
    def __str__(self):
        return self.nombre


class auxiliares(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre", max_length=50)
    Grupo_de_Investigación_al_que_Pertenece=models.ForeignKey( grupos_de_investigacion, null=False, on_delete=models.CASCADE)
    proyecto_de_investigacion = models.CharField("Proyecto de Investigación", max_length=200)

    investigadores_vinculados= models.ForeignKey( investigadores, null=True, on_delete=models.CASCADE)

    anio_vinculacion = models.PositiveIntegerField("Año de Vinculación")
    nombre_Asesor = models.CharField("Nombre Asesor", max_length=50)
    
    programa = [
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

    programa_academico=models.CharField("Programa Académico", max_length=41, choices=programa, default="INGENIERÍA DE SISTEMAS", null=True, blank=True)
    correo = models.EmailField("Correo", blank=True)
    telefono = models.PositiveIntegerField("Teléfono", blank=True)

    class Meta:
        verbose_name = "Auxiliar"
        verbose_name_plural = "Auxiliares"
    
    def __str__(self):
        return self.nombre


class pasantes(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre", max_length=50)
    Grupo_de_Investigación_al_que_Pertenece=models.ForeignKey(grupos_de_investigacion, null=False, on_delete=models.CASCADE)
    proyecto_de_investigacion = models.CharField("Proyecto de Investigación", max_length=200)

    investigadores_vinculados= models.ForeignKey( investigadores, null=True, on_delete=models.CASCADE)

    anio_vinculacion = models.PositiveIntegerField("Año Vinculación")
    nombre_Asesor = models.CharField("Nombre del Asesor", max_length=50)
    
    programa = [
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

    programa_academico=models.CharField("Programa Académico", max_length=41, choices=programa, default="INGENIERÍA DE SISTEMAS", null=True, blank=True)
    correo = models.EmailField("Correo", blank=True)
    telefono = models.PositiveIntegerField("Teléfono", blank=True)

    class Meta:
        verbose_name = "Pasante"
        verbose_name_plural = "Pasantes"

    def __str__(self):
        return self.nombre


class jovenes_investigadores(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    Grupo_de_Investigación_al_que_Pertenece=models.ForeignKey(grupos_de_investigacion, null=False, on_delete=models.CASCADE)
    proyecto_de_investigación = models.CharField(max_length=200)

    investigadores_vinculados= models.ForeignKey(investigadores, null=True, on_delete=models.CASCADE)

    año_vinculación = models.PositiveIntegerField()
    nombre_Asesor = models.CharField(max_length=50)
    
    programa = [
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

    programa_académico=models.CharField(max_length=41, choices=programa, default="INGENIERÍA DE SISTEMAS", null=True, blank=True)

    correo = models.EmailField(blank=True)
    teléfono = models.PositiveIntegerField(blank=True)

    class Meta:
        verbose_name = "joven investigador"
        verbose_name_plural = "jovenes Investigadores"

    def __str__(self):
        return self.nombre


class estudiantes_trabajo_grado(models.Model):

    id = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    Numero_de_Identificación=models.PositiveIntegerField()
    nombre_del_Proyecto=models.CharField(max_length=200)
    programa = [
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

    programa_Académico=models.CharField(max_length=41, choices=programa, null=True, blank=True)
    nombre_Asesor=models.CharField(max_length=50)
    correo = models.EmailField(blank=True)
    teléfono = models.PositiveIntegerField(blank=True)

    class Meta:
        verbose_name = "Estudiante Trabajo de Grado"
        verbose_name_plural = "Estudiantes Trabajo de Grado"

    def __str__(self):
        return self.nombre