import os
from . import dj_database_url

from .base import *
ROOT_URLCONF = 'church.urls'
CORS_REPLACE_HTTPS_REFERER = True
HOST_SCHEME = "https://"
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 1000000

SECURE_FRAME_DENY = True


"""
Production Settings for Heroku
"""

# If using in your own project, update the project namespace below

# env = os.environ.get('DEBUG')
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

# False if not in os.environ
# DEBUG = env('DEBUG')

# Parse database connection url strings like psql://user:pass@127.0.0.1:8458/db


db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES=['default'].update(db_from_env)

# DATABASES = {
#     # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
#     'default': env.db(),
# }


# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = os.environ('SECRET_KEY')

ALLOWED_HOSTS = ['https://frymn-church.herokuapp.com']


