from django.contrib import admin
from .models import convocatorias_internas, convocatorias_externas

# Register your models here.

class buscarconvocatorias(admin.ModelAdmin):
    list_display = ('nombre_convocatoria', 'estado', 'fecha_de_Inicio', 'fecha_Finalizacion', 'monto_ganadores')
    search_fields = ('estado', 'nombre_convocatoria', 'fecha_de_Inicio', 'fecha_Finalizacion')
    date_hierarchy = 'fecha_de_Inicio'
    list_filter = ('estado', 'nombre_convocatoria')
    list_per_page=20


admin.site.register(convocatorias_internas, buscarconvocatorias)
admin.site.register(convocatorias_externas, buscarconvocatorias)


# Define el orden de las aplicaciones
admin.site.order = (
    ('investigadores', 'Investigadores'),
    ('formacion_investigativa', 'Formacion_investigativa'),
    ('convocatorias', 'Convocatorias'),
)