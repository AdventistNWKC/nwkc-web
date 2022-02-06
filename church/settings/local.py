from .base import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'me22pc=!rx)*17h&)sb&h-)^tl9u0f+z(ifwlxtdla)ad%-9yp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'frymn-church.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.sqlite3',
# #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
# #     }
# # }

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'wkcdb',
            'USER': 'postgres',
            'PASSWORD': 'Admin',
            'HOST': 'localhost',
            'PORT': '',
        }
    }




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

