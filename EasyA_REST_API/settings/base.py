__author__ = 'TimCardwell'

"""
Django settings for EasyA_REST_API project.

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
# https://docs.djangoproject.com/en/1.8/topics/signing/
SECRET_KEY = '-2#g_0d!b&_q)f!7l_8r+y^^1qmw)10hb7$mgdpvqp^pctjegv'

ALLOWED_HOSTS = []

STATIC_URL = '/static/'

# Application definition

INSTALLED_APPS = (
    'rest_framework',
    'rest_api',
    #'django.contrib.admin', While this is nice, I don't want it in here
    #'django.contrib.auth',
    #'django.contrib.contenttypes',
    #'django.contrib.sessions', Don't need sessions in a REST API
    #'django.contrib.messages', Don't need messaging in a REST API
    'django.contrib.staticfiles'
)

MIDDLEWARE_CLASSES = (
    #'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#REST_FRAMEWORK = {
#    'DEFAULT_PERMISSION_CLASSES': [
#        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#    ]
#}

ROOT_URLCONF = 'EasyA_REST_API.urls'

WSGI_APPLICATION = 'EasyA_REST_API.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_TZ = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

DEFAULT_CONTENT_TYPE = 'application/json'