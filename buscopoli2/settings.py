import os  # isort:skip
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for buscopoli2 project.

Generated by 'django-admin startproject' using Django 3.1.14.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

import pymysql

pymysql.install_as_MySQLdb()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8t%dgnw)-5qp#$y**gd(z+v($xnoj66+!1yqj+g(d(cwvw$3t4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition





ROOT_URLCONF = 'buscopoli2.urls'



WSGI_APPLICATION = 'buscopoli2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases




# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

#----------------------------------------------- correo-----------------------------------------------

CMS_TOOLBAR = True
CMS_TOOLBAR_SITE_NAME = 'SIGIM'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'mquenoran@umariana.edu.co'
EMAIL_HOST_PASSWORD = '1004596855Marlonn'
DEFAULT_FROM_EMAIL = 'mquenoran@umariana.edu.co'
EMAIL_USE_SSL = False


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATIC_TMP = os.path.join(BASE_DIR, 'static')

os.makedirs(STATIC_TMP, exist_ok=True)
os.makedirs(STATIC_ROOT, exist_ok=True)

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'buscopoli2', 'static'),
)
SITE_ID = 1


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
        },
    },
]


MIDDLEWARE = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware' #nueva
    'whitenoise.middleware.WhiteNoiseMiddleware' #nueva
]

INSTALLED_APPS = [


    'django.contrib.redirects',     #nueva
    #'ckeditor',                    #nueva
    #'ckeditor_uploader',           #nueva
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    'djangocms_bootstrap4',
    'djangocms_bootstrap4.contrib.bootstrap4_alerts',
    'djangocms_bootstrap4.contrib.bootstrap4_badge',
    'djangocms_bootstrap4.contrib.bootstrap4_card',
    'djangocms_bootstrap4.contrib.bootstrap4_carousel',
    'djangocms_bootstrap4.contrib.bootstrap4_collapse',
    'djangocms_bootstrap4.contrib.bootstrap4_content',
    'djangocms_bootstrap4.contrib.bootstrap4_grid',
    'djangocms_bootstrap4.contrib.bootstrap4_jumbotron',
    'djangocms_bootstrap4.contrib.bootstrap4_link',
    'djangocms_bootstrap4.contrib.bootstrap4_listgroup',
    'djangocms_bootstrap4.contrib.bootstrap4_media',
    'djangocms_bootstrap4.contrib.bootstrap4_picture',
    'djangocms_bootstrap4.contrib.bootstrap4_tabs',
    'djangocms_bootstrap4.contrib.bootstrap4_utilities',
    'djangocms_file',
    'djangocms_icon',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_style',
    'djangocms_googlemap',
    'djangocms_video',
    'buscopoli2',
    'convocatorias',
    'formacion_investigativa.apps.FormacionInvestigativaConfig',
    'investigadores',
    'import_export',
    'user',
    'login'



]

CKEDITOR_UPLOAD_PATH = 'content/ckeditor/'

LANGUAGES = [
    ('en', ('English')),
    ('es', ('Spanish'))
    # Otros idiomas que desees admitir
]


#nueva
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),  # Carpeta para las traducciones
)


CMS_LANGUAGES = {
    ## Customize this
    #1: [
    #    {
    #        'code': 'es',
    #        'name': gettext('es'),
    #        'redirect_on_fallback': True,
    #        'public': True,
    #        'hide_untranslated': False,
    #    },
    #],
    #'default': {
    #    'redirect_on_fallback': True,
    #    'public': True,
    #    'hide_untranslated': False,
    #},


    1: [
            {
                'code': 'en',
                'name': ('English'),
                'fallbacks': ['es'],  # Idioma de respaldo si no se encuentra una traducción
                'public': True,
                'hide_untranslated': False,
                'redirect_on_fallback': True,
            },
            {
                'code': 'es',
                'name': ('Spanish'),
                'fallbacks': ['en'],
                'public': True,
                'hide_untranslated': False,
                'redirect_on_fallback': True,
            },
        ],
        'default': {
            'fallbacks': ['en', 'es'],  # Idiomas a utilizar si no se encuentra una traducción
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },


}

CMS_TEMPLATES = (
    ## Customize this


    ('prueba-datos.html', 'prueba datos'),
    ('guardado-exitoso.html', 'Guardado Exitoso'),
    ('login.html', 'ventana login'),
    ('HOME.html', 'home Prueba'),
    ('Investigación--Estrictaa.html', 'Ventana Investigación Estricta'),
    ('grupos.html', 'Ventana Grupos Prueba'),
    ('grupos-final.html', 'Ventana Grupos'),
    ('resultados.html', 'Ventana resultados nulos'),
    ('acta_inicio.html', 'acta de inicio'),
    ('perfil-investigador.html', 'Perfil Investigador'),
    ('Datos_Generales.html', 'Perfil Datos Generales'),
    ('proyecto_innovacion.html', 'Proyecto Innovación'),
    ('proyecto_cientifico.html', 'Proyecto Cientifico'),
    ('proyecto_tecnologico.html', 'Proyecto Tecnologico'),
    ('convocatoria-interna.html', 'Convocatorias Internas'),
    ('convocatoria_interna_parte2.html', 'Información Convocatoria Interna'),
    ('convocatoria-externa.html', 'Convocatorias Externas'),
    ('convocatoria_externa_parte2.html', 'Informacion Convocatoria Externa'),
    ('resultados_investigacion.html', 'Ventana Resultados'),
    ('perfil-admin.html', 'Ventana Perfil Administrador'),
    ('fullwidth.html', 'Fullwidth'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right')


)

X_FRAME_OPTIONS = 'SAMEORIGIN'

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'buscopoli',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',

        #'OPTIONS': {
        #    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        #},
    }
}

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'