from .base import *
#from .INFO import S_KEY


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('S_KEY')


DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'plateforme',
        'USER': 'postgres',
        'PASSWORD': "firefighter77@",
        'HOST': '',
        'PORT': '5432',
    }
}
