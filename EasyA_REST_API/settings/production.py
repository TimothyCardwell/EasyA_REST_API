__author__ = 'TimCardwell'


from EasyA_REST_API.settings.base  import *

DEBUG = False

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


# Security
# Because a settings file contains sensitive information, such as the database password
# you should make every attempt to limit access to it. For example, change its file
# permissions so that only you and your Web server’s user can read it. This is especially
# important in a shared-hosting environment.

# CSRF
# See the CSRF_* settings
# https://docs.djangoproject.com/en/1.8/ref/csrf/

# Caching
# See the CACHES setting
# https://docs.djangoproject.com/en/1.8/topics/cache

# Error Reporting
# See the ADMINS setting
# https://docs.djangoproject.com/en/1.8/howto/error-reporting/

# Emails
# https://docs.djangoproject.com/en/1.8/topics/email/

# Localization
# See the LANGUAGES setting
# https://docs.djangoproject.com/en/1.8/topics/i18n/