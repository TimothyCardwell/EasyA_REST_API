__author__ = 'TimCardwell'

from EasyA_REST_API.settings.base  import *
import sys

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'rest_api_admin',
        'PASSWORD': 'Playstation3',
        'NAME': 'easy_a',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/easy_a.log'),
            'formatter': 'simple'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'propagate': True,
            'level': 'DEBUG',
        },

        # TODO This isn't working
        'django.request': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}

# Authentication
# See the Auth section in https://docs.djangoproject.com/en/1.8/ref/settings/
# When the time comes to implement authentication into this API
# https://docs.djangoproject.com/en/1.8/topics/auth/#module-django.contrib.auth

# TODO Import database at least, what else?

# MEDIA_ROOT
# Defines where stored files will go
# https://docs.djangoproject.com/en/1.8/topics/files/
# Security for this setting https://docs.djangoproject.com/en/1.8/topics/security/#user-uploaded-content-security
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'