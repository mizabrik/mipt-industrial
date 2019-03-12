from djangotodo.settings.common import *

SECRET_KEY = 'ilovepromprog'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'db',
        'NAME': 'postgres',
        'USER': 'postgres',
    }
}


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
