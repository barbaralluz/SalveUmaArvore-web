# -*- coding: utf-8 -*-
"""
Django settings for tg project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x(upjz8tun_o_@32^omf(zu=2lyhox(&ycfgao%8vb@x2lkhs*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tg.core',
    'municipios',
    'social_auth',
    'django.contrib.gis',
    'django_user_agents',
    'django.contrib.sites',
    'fluent_comments',
    'crispy_forms',
    'django_comments',

)

COMMENTS_APP = 'fluent_comments'
FLUENT_COMMENTS_EXCLUDE_FIELDS = ('name', 'email', 'url')
FLUENT_COMMENTS_AKISMET_ACTION = 'delete' 

SITE_ID = 1

# Name of cache backend to cache user agents. If it not specified default
# cache alias will be used. Set to `None` to disable caching.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'social_auth.context_processors.social_auth_by_type_backends',
)

TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader',
 'django.template.loaders.app_directories.Loader')

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
)


MUNICIPIOS_GEO = True

FACEBOOK_APP_ID              = '748657411909785'
FACEBOOK_API_SECRET          = '7b2c5ae08276a49bc26d52a943a4f9d4'
FACEBOOK_EXTENDED_PERMISSIONS = ['email']

GOOGLE_OAUTH2_CLIENT_ID  = '184120370259-06c93doeviuph4nvlu1jj4fglhd4s7rb.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET = 'LCzMnVkHWnl3GtJ1wcvAuZsr'

SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
)

ROOT_URLCONF = 'tg.urls'

WSGI_APPLICATION = 'tg.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis', 
        'NAME': 'geology',                     
        'USER': 'geouser',
        'PASSWORD': 'geopassword',
        'HOST': 'localhost',                      
        'PORT': '',                
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, '../templates/'),
)

MEDIA_ROOT = 'tg/core/media/'

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

LOGIN_URL = "/login/"
LOGOUT_URL = "/logout/"
LOGIN_REDIRECT_URL = "/list/tree/"

# configurando o usuario do django para ser
# o usuario definido pelo projeto e nao o usuario
# padrao do Django.contrib.auth
AUTH_PROFILE_MODULE = 'tg.core.Profile'
