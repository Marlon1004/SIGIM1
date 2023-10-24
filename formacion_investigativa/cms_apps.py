from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class formacion(CMSApp):
    app_name = "Formacion Investigativa"
    name = _("FORMACION INVESTIGATIVA")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["formacion_investigativa.urls"]


apphook_pool.register(formacion)  # registro de la application