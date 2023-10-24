from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models  import  investigadores, proyecto_Innovacion, grupos_de_investigacion, compromiso,  \
    entidade, proyecto_Cientifico, proyecto_Tecnologico, ModeloPrueba

# Register your models here.


admin.site.register(ModeloPrueba)

class entidadesResources(resources.ModelResource):

    skip_unchanged = True
    report_skipped = True
    class Meta:
        model = entidade


class buscarentidades(ImportExportModelAdmin):
    list_display = ('nombre', 'numero_Contrato')
    search_fields = ('nombre', 'numero_Contrato')
    date_hierarchy = 'fecha_suscripcion'
    list_filter = ('nombre', 'numero_Contrato')
    list_per_page=20
    resource_class = entidadesResources

admin.site.register(entidade, buscarentidades)


#----------------------------------------------------------------

class gruposResources(resources.ModelResource):

    skip_unchanged = True
    report_skipped = True
    class Meta:
        model = grupos_de_investigacion


class buscargruposdeinvestigacion(ImportExportModelAdmin):
    list_display = ('codigo', 'nombre_Grupo', 'lider', 'linea_investigacion' )
    search_fields = ('codigo', 'nombre_Grupo', 'lider', 'linea_investigacion')
    date_hierarchy = 'fecha_Formacion'
    list_filter = ('codigo', 'nombre_Grupo')
    list_per_page=20
    resource_class = gruposResources

admin.site.register(grupos_de_investigacion, buscargruposdeinvestigacion)

#----------------------------------------------------------------

#----------------------------------------------------------------

class buscarcompromisos(admin.ModelAdmin):
    list_display = ('codigo', 'producto', 'cantidad', 'medio_de_verificacion')
    search_fields = ('codigo', 'producto')
    date_hierarchy = 'fecha'
    list_filter = ('codigo', 'producto')
    list_per_page=20

admin.site.register(compromiso, buscarcompromisos)


#--------------------------------------------------------------------------------------------

class productosResources(resources.ModelResource):

    skip_unchanged = True
    report_skipped = True
    class Meta:
        model = proyecto_Innovacion


class buscarproductosInnovacion(ImportExportModelAdmin):
    list_display = ('id', 'nombre_proyecto', 'grupo_de_Investigacion1', 'fecha_de_Inicio', 'facultad' )
    search_fields = ('id', 'nombre_proyecto')
    date_hierarchy = 'fecha_de_Inicio'
    list_filter = ('id', 'nombre_proyecto')
    list_per_page=20
    resource_class = productosResources

admin.site.register(proyecto_Innovacion, buscarproductosInnovacion)

#----------------------------------------------------------------------------------------------


class productosResources(resources.ModelResource):

    skip_unchanged = True
    report_skipped = True
    class Meta:
        model = proyecto_Tecnologico


class buscarproductosTecnologicos(ImportExportModelAdmin):
    list_display = ('id', 'nombre_proyecto', 'facultad' )
    search_fields = ('id', 'nombre_proyecto')

    list_filter = ('id', 'nombre_proyecto')
    list_per_page=20
    resource_class = productosResources

admin.site.register(proyecto_Tecnologico, buscarproductosTecnologicos)


#----------------------------------------------------------------------------------------------

class productosResources(resources.ModelResource):

    skip_unchanged = True
    report_skipped = True
    class Meta:
        model = proyecto_Cientifico


class buscarproductosCientificos(ImportExportModelAdmin):
    list_display = ('id', 'nombre_proyecto', 'fecha_Convocatoria', 'facultad' )
    search_fields = ('id', 'nombre_proyecto')
    date_hierarchy = 'fecha_Convocatoria'
    list_filter = ('id', 'nombre_proyecto')
    list_per_page=20
    resource_class = productosResources

admin.site.register(proyecto_Cientifico, buscarproductosCientificos)

#----------------------------------------------------------------------------------------------

class investigadoresResources(resources.ModelResource):
    fields =(
        'id',
        'nombres_completos',
        'cedula',
        'grupo_de_Investigacion',
        'facultad_adscrito',
        'gmail',
        'estado',
    )
    exclude = ('id',)
    skip_unchanged = True
    report_skipped = True
    class Meta:
        model = investigadores


class buscarinvestigadores(ImportExportModelAdmin):
    list_display = ('cedula', 'nombres_completos', 'grupo_de_Investigación', 'facultad_adscrito', 'gmail', 'estado' )
    search_fields = ('cedula', 'nombres_completos')
    resource_class = investigadoresResources
    list_filter = ('cedula', 'nombres_completos')
    list_per_page=20



admin.site.register(investigadores, buscarinvestigadores)


# Define el orden de las aplicaciones
admin.site.order = (
    ('investigadores', 'Investigadores'),
    ('formacion_investigativa', 'Formacion_investigativa'),
    ('convocatorias', 'Convocatorias'),
)
