# miapp/cms_plugins.py
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from . import views
#from .views import MiModelo


class MiVistaPlugin(CMSPluginBase):
    #model = MiModelo                              # Deja esto como None si no necesitas guardar información adicional para el plugin.
    render_template = "login.html"  # Ruta de la plantilla que mostrará la vista.
    name = _("plugin de login")                # Nombre amigable para el plugin en la administración
    cache = False                              # Deja esto como False si tu vista es dinámica y puede cambiar en cada solicitud.

    def render(self, context, instance, placeholder):
        # Aquí puedes agregar lógica adicional antes de mostrar la vista.
        context['content'] = views.login_view(context['request'])  # Llamamos a la vista de Django definida en views.py
        return context

plugin_pool.register_plugin(MiVistaPlugin)
