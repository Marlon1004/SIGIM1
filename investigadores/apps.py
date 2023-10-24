from django.apps import AppConfig


class InvestigadoresConfig(AppConfig):

    name = 'investigadores'

    def ready(self):
        import investigadores.signals  # Importa el archivo signals.py de tu_app




