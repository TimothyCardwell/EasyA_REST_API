from EasyA_REST_API.settings.base  import *

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': '',
        'USER': '',
        'PASSWORD': '',
        'NAME': 'easy_a',
    }
}

LOGGING = {}

# TODO Import database at least, what else?