from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from .views import SaleInvoicePdfView, generar_pdf, generar_pdf2, login_view2, guardar_datos
from cms.urls import urlpatterns as cms_urls
from django.views.generic import TemplateView
from django.urls import re_path
from buscopoli2 import views




admin.autodiscover()

urlpatterns = [

    #path('', views.home_view, name='home'),
    #re_path(r'^admin/', admin.site.urls),
    path('cms/', include(cms_urls)), #no quitar
    path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}), #viene por defecto


    #path('accounts/login/',  login_view, name='login_view'),

#--------------------------------------------------------------------------------------------
    #path('logout/', logout_view, name='logout'),

    #path("accounts/", include("django.contrib.auth.urls")),

    #----------crear pdf--------------------------------


    path('generar-pdf/', generar_pdf, name='generar_pdf'),
    path('generar-pdf2/', generar_pdf2, name='generar_pdf2'),
    path('login_view2/', login_view2, name='login_view2'),
    path('guardar_datos/', guardar_datos, name='guardar_datos'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),                            # Asegúrate de incluir el admin
    path("", include("cms.urls")),                          # URLs de Django CMS
    path('filer/', include('filer.urls')),                      # URLs de Filer
    #path('ckeditor/', include('ckeditor_uploader.urls')),       # URLs de CKEditor



    path("accounts/", include("django.contrib.auth.urls"))


    )




# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
