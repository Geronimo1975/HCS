from .base import *  # we need to extend our base
import environ

env = environ.Env()
environ.Env.read_env(str(BASE_DIR.parent / '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PWD'),
        'HOST': env.str('DB_HOST'),
        'PORT': env.str('DB_PORT'),
    }
}

# Stripe API Keys 
STRIPE_PUBLIC_KEY = env.str("STRIPE_PUBLIC_KEY")
STRIPE_SECRET_KEY = env.str("STRIPE_SECRET_KEY")
# Paypal API Keys 
PAYPAL_CLIENT_ID = env.str('PAYPAL_CLIENT_ID')
PAYPAL_SECRET_ID = env.str('PAYPAL_SECRET_ID')



ANYMAIL = {
    #"MAILGUN_API_KEY": os.environ.get("MAILGUN_API_KEY"),
    #"MAILGUN_SENDER_DOMAIN": os.environ.get("MAILGUN_SENDER_DOMAIN"),
    "MAILJET_API_KEY": "dein_mailjet_api_key",
    "MAILJET_SECRET": "dein_mailjet_secret",
}

EMAIL_BACKEND = "anymail.backends.mailjet.EmailBackend"

FROM_EMAIL = env.str('FROM_EMAIL')
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD')
EMAIL_BACKEND = env.str('EMAIL_BACKEND')
DEFAULT_FROM_EMAIL = env.str('DEFAULT_FROM_EMAIL')
SERVER_EMAIL = os.getenv("SERVER_EMAIL", DEFAULT_FROM_EMAIL)
# SERVER_EMAIL = env.str('SERVER_EMAIL')