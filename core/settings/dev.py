from django.conf.global_settings import EMAIL_BACKEND

from .base import  *


DEBUG = env.bool("DEBUG", default=True)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["127.0.0.1", "localhost"])

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"