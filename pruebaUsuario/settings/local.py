import os
from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'dauobm2777lbss',
    'USER': 'ygzbxaqexwjfsw',
    'PASSWORD': 'c6c1587c40f318b5abb4eeeb3eccb39541429ceae6290749c01e146a761f2689',
    'HOST': 'ec2-3-231-69-204.compute-1.amazonaws.com',
    'PORT': '5432',
    }
}
STATIC_URL = '/static/'

