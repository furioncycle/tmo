import json, os, sys
from .base import *
from tmo.env import env

DEBUG = env.bool("DJANGO_DEBUG", default=False)

ALLOWED_HOSTS = [
    'tmo.app.cloud.gov'
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

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
    },
}
