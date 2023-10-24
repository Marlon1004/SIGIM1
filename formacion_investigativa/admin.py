from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models  import  semillerista, proyecto_semillerista, eventos_Relacionados, semillero, \
    jovenes_investigadores, coInvestigadores, auxiliares, pasantes, estudiantes_trabajo_grado


# Register your models here.


class buscareventosrelacionados(admin.ModelAdmin):
    list_display = ('eventos_Nacionales', 'eventos_Internacionales')  # Ahora la interfaz mostrará nombre, apellido y email de cada autor.
    search_fields = ('eventos_Nacionales', 'eventos_Internacionales')
    
    list_filter = ('eventos_Nacionales', 'eventos_Internacionales', 'Grupo_de_Investigación')
    list_per_page=20

admin.site.register(eventos_Relacionados,buscareventosrelacionados)

#-----------------------------------------------------------------

class proyectossemilleristasResources(resources.ModelResource):

    skip_unchanged = True
    report_skipped = True
    class Meta:
        model = proyecto_semillerista


class buscarproyectosemillerista(ImportExportModelAdmin):
    list_display = ('Nombre_del_Proyecto', 'codigo_Proyecto',  'estado_del_Proyecto', 'linea_de_Investigacion', 'convalidado' )
    search_fields = ('codigo_Proyecto', 'Nombre_del_Proyecto')
    
    list_filter = ('codigo_Proyecto', 'Nombre_del_Proyecto')
    list_per_page=20

    resource_class = proyectossemilleristasResources

admin.site.register(proyecto_semillerista, buscarproyectosemillerista)


#-----------------------------------------------------------------

class semilleristasResources(resources.ModelResource):

    skip_unchanged = True
    report_skipped = True
    class Meta:
        model = semillerista


class buscarsemillerista(ImportExportModelAdmin):
    list_display = ( 'nombre_Completo', 'cedula', 'codigo_Proyecto', 'semillero', 'codigo_Estudiantil', 'correo' )  
    search_fields = ('cedula', 'nombre_Completo')
    date_hierarchy = 'fecha_Vinculacion'
    list_filter = ('cedula', 'nombre_Completo')
    list_per_page=20

    resource_class = semilleristasResources


admin.site.register(semillerista,buscarsemillerista)

#-----------------------------------------------------------------

class semillerosResources(resources.ModelResource):

    skip_unchanged = True
    report_skipped = True
    class Meta:
        model = semillero

class buscarsemillero(ImportExportModelAdmin):
    list_display = ('nombre', 'coordinador', 'lider_Semillero', 'linea_Investigacion', 'programa' )
    search_fields = ('nombre', 'coordinador')
    date_hierarchy = 'fecha_de_Creacion'
    list_filter = ('nombre', 'coordinador')
    list_per_page=20

    resource_class = semillerosResources

admin.site.register(semillero, buscarsemillero)


#-----------------------------------------------------------------

class coinvestigadoresResources(resources.ModelResource):

    skip_unchanged = True
    report_skipped = True
    class Meta:
        model = coInvestigadores


class buscarcoinvestigadores(ImportExportModelAdmin):
    list_display = ('nombre', 'nombre_Asesor', 'Grupo_de_Investigación_al_que_Pertenece', 'programa_academico', 'anio_vinculacion' )
    search_fields = ('nombre', 'nombre_Asesor')
    
    list_filter = ('nombre', 'nombre_Asesor')
    list_per_page=20

    resource_class = coinvestigadoresResources

admin.site.register(coInvestigadores, buscarcoinvestigadores)

#-----------------------------------------------------------------

class jovenesinvestigadoresResources(resources.ModelResource):

    skip_unchanged = True
    report_skipped = True
    class Meta:
        model = jovenes_investigadores


class buscarjovenesinvestigadores(ImportExportModelAdmin):
    list_display = ('nombre', 'nombre_Asesor', 'Grupo_de_Investigación_al_que_Pertenece', 'programa_académico', 'año_vinculación' )  
    search_fields = ('nombre', 'nombre_Asesor')
    
    list_filter = ('nombre', 'nombre_Asesor')
    list_per_page=20

    resource_class = jovenesinvestigadoresResources

admin.site.register(jovenes_investigadores,buscarjovenesinvestigadores)


#-----------------------------------------------------------------

class auxiliaresResources(resources.ModelResource):

    skip_unchanged = True
    report_skipped = True
    class Meta:
        model = auxiliares

class buscarauxiliares(ImportExportModelAdmin):
    list_display = ('nombre', 'nombre_Asesor', 'Grupo_de_Investigación_al_que_Pertenece', 'programa_academico', 'anio_vinculacion' )
    search_fields = ('nombre', 'nombre_Asesor')
    
    list_filter = ('nombre', 'nombre_Asesor')
    list_per_page=20

    resource_class = auxiliaresResources

admin.site.register(auxiliares, buscarauxiliares)

#-----------------------------------------------------------------

class pasantesResources(resources.ModelResource):

    skip_unchanged = True
    report_skipped = True
    class Meta:
        model = pasantes

class buscarpasantes(ImportExportModelAdmin):
    list_display = ('nombre', 'nombre_Asesor', 'Grupo_de_Investigación_al_que_Pertenece', 'programa_academico', 'anio_vinculacion' )
    search_fields = ('nombre', 'nombre_Asesor')
    
    list_filter = ('nombre', 'nombre_Asesor')
    list_per_page=20

    resource_class = pasantesResources


admin.site.register(pasantes, buscarpasantes)


#-----------------------------------------------------------------

class estudiantestrabajodegradoResources(resources.ModelResource):

    skip_unchanged = True
    report_skipped = True
    class Meta:
        model = estudiantes_trabajo_grado

class buscarportrabajodegrado(ImportExportModelAdmin):
    list_display = ('nombre', 'Numero_de_Identificación', 'programa_Académico' )  
    search_fields = ('nombre', 'Numero_de_Identificación')
    
    list_filter = ('nombre', 'Numero_de_Identificación')
    list_per_page=20

    resource_class = estudiantestrabajodegradoResources

admin.site.register(estudiantes_trabajo_grado, buscarportrabajodegrado)


# Define el orden de las aplicaciones
admin.site.order = (
    ('investigadores', 'Investigadores'),
    ('formacion_investigativa', 'Formacion_investigativa'),
    ('convocatorias', 'Convocatorias'),
)
