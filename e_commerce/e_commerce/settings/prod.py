import os

from e_commerce.settings.base import *

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "e_commerce"),
        "HOST": "localhost",
        "PORT": "5432",
    }
}
