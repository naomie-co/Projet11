from .base import *
from .INFO import S_KEY



DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = S_KEY