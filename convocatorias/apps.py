from django.apps import AppConfig


class ConvocatoriasConfig(AppConfig):
    name = 'convocatorias'

    def ready(self):
        import convocatorias.signals  # Importa el archivo signals.py de tu_app