from django.apps import AppConfig


class FormacionInvestigativaConfig(AppConfig):
    name = 'formacion_investigativa'
    verbose_name= 'Formación Investigativa'

    def ready(self):
        import formacion_investigativa.signals  # Importa el archivo signals.py de tu_app