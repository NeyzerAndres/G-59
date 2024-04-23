from .base import *

DEBUG = True
ALLOWED_HOSTS = []
WSGI_APPLICATION = 'Empleado.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

