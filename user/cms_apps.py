from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class user(CMSApp):
    app_name = "User"
    name = _("USER  ")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["user.urls"]


apphook_pool.register(user)  # registro de la application