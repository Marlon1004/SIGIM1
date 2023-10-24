from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class convocatorias(CMSApp):
    app_name = "convocatorias"
    name = _("CONVOCATORIAS")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["convocatorias.urls"]


apphook_pool.register(convocatorias)  # registro de la application