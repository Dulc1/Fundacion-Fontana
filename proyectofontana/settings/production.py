from .base import *
import os
import dj_database_url
import django_heroku

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = False

CSRF_TRUSTED_ORIGINS = [ 'https://proyectofinalsupersayayin2.herokuapp.com' ]

DEBUG_PROPAGATE_EXCEPTIONS = True

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_pyscopg2',
        'NAME': 'django-pbpostgres',
        'USER': 'name',
        'PASSWORD':'',
        'HOST': 'localhost',
        'PORT':'',
    }
}

db_from_env= dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
django_heroku.settings(locals())

STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_STORAGE='whitenoise.storage.CompressedStaticFilesStorage'


STATIC_URL = 'https://proyectofinalsupersayayin2.herokuapp.com/static/'
MEDIA_URL = 'https://proyectofinalsupersayayin2.herokuapp.com/media/'