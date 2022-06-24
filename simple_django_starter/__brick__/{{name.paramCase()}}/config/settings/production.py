from datetime import timedelta

from django.core.management.utils import get_random_secret_key


from .base import *


# * Quick-start development settings - unsuitable for production
# ? See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_random_secret_key()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Allowed hosts
ALLOWED_HOSTS = ['*']


# * Database
# ? https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': os.environ['DATABASE_ENGINE'],
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': os.environ['DATABASE_PORT'],
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


# * Documentation configuration
# ? https://docs.djangoproject.com/en/4.0/topics/email
# ? https://www.geeksforgeeks.org/setup-sending-email-in-django-project/

# *Twilio configuration
# ? https://www.twilio.com/blog/using-twilio-sendgrid-send-emails-python-django

# Email configuration - for development purposes only (Gmail)
# Twilio SendGrid
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
FROM_EMAIL = os.environ['SEND_GRID_VERIFY_MAIL']
DEFAULT_FROM_EMAIL = os.environ['SEND_GRID_VERIFY_MAIL']
SENDGRID_ECHO_TO_STDOUT = True
SENDGRID_API_KEY = os.environ['SEND_GRID_API_KEY']
SENDGRID_SANDBOX_MODE_IN_DEBUG = False