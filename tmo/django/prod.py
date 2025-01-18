import json, os, sys
from .base import *
from tmo.env import env

DEBUG = env.bool("DJANGO_DEBUG", default=False)

ALLOWED_HOSTS = [
    'http://tmo.app.cloud.gov'
]
#env.list("ALLOWED_HOSTS", default=[])

creds = json.loads(os.getenv('VCAP_SERVICES'))['user-provided'][0]['credentials']
SECRET_KEY = creds['SECRET_KEY']

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': env.db('DATABASE_URL')
# }
# 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
