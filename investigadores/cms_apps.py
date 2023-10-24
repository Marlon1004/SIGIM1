from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class investigadores(CMSApp):
    app_name = "Investigadores"
    name = _("INVESTIGADORES")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["investigadores.urls"]


apphook_pool.register(investigadores)  # registro de la application