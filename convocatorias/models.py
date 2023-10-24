from django.db import models

# Create your models here.

class convocatorias_internas(models.Model):

    id = models.AutoField(primary_key=True)
    esta = [
        ("ACTIVA", "ACTIVA"),
        ("INACTIVA", "INACTIVA")

    ]
    estado=models.CharField("Estado", max_length=10, choices=esta, default="ACTIVA")
    nombre_convocatoria=models.CharField("Nombre de la Convocatoria", max_length=200)
    fecha_de_Inicio=models.DateField("Fecha de Inicio")
    fecha_Finalizacion=models.DateField("Fecha de Finalización")
    monto_ganadores=models.PositiveIntegerField("Monto Ganadores")

    documentos_del_Proceso=models.FileField("Subir documentos del Proceso", upload_to='media/convocatorias_interna/')

    class Meta:
        verbose_name = "Convocatoria Interna"
        verbose_name_plural = "Convocatorias Internas"


class convocatorias_externas(models.Model):

    id = models.AutoField(primary_key=True)
    esta = [
        ("ACTIVA", "ACTIVA"),
        ("INACTIVA", "INACTIVA")

    ]
    estado = models.CharField("Estado", max_length=10, choices=esta, default="ACTIVA")
    nombre_convocatoria = models.CharField("Nombre de la Convocatoria",max_length=200)
    fecha_de_Inicio = models.DateField("Fecha de Inicio",)
    fecha_Finalizacion = models.DateField("Fecha de Finalización")
    enlace_Externo = models.URLField("Enlace Externo")
    monto_ganadores = models.PositiveIntegerField("Monto Ganadores")
    documentos_del_Proceso=models.FileField("Subir Documentos del Proceso", upload_to='media/convocatorias_externa/')

    class Meta:
        verbose_name = "Convocatoria Externa"
        verbose_name_plural = "Convocatorias Externas"