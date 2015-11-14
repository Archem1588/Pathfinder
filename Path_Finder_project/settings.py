"""
Django settings for PathFinder project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1#57$imgw8-pc@p73gb3#58qt%+f2#oodl-o)(r0_^5lq!*0i3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Email Setup

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'tomato.pathfinder@gmail.com'
EMAIL_HOST_PASSWORD = 'Pathfinder'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# if emails still don't go through, try unlocking captcha:
# https://accounts.google.com/displayunlockcaptcha
# https://www.google.com/settings/security/lesssecureapps

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bikeways',
    'registration',
    'crispy_forms',
    'social.apps.django_app.default',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'Path_Finder_project.urls'

# Had to change every django.template(s) to django.template (without 's')
templateDir = os.path.dirname(__file__)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.core.context_processors.csrf',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'Path_Finder_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tomato',
        'USER': 'postgres',
    }
}


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES['default'] = dj_database_url.config(default='postgres://yccapuatcylbhs:yN4k4RVMIBiQfWwLamKfBiyZ_C@ec2-107-21-221-107.compute-1.amazonaws.com:5432/d8v71h5394a9ht')
DATABASES['default']['ENGINE'] = 'django_postgrespool'
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'tomato',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         'HOST': '',
#         'PORT': '',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
#     }
# }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Account Login and Registration Settings

ACCOUNT_ACTIVATION_DAYS = 7     # One-week activation window.
REGISTRATION_AUTO_LOGIN = True  # Automatically log the user in.
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

#Crispy FORM TAGs SETTINGS
CRISPY_TEMPLATE_PACK = 'bootstrap3'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_in_pro", "our_static"),
    #os.path.join(BASE_DIR, "static_in_env"),
    #'/var/www/static/',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "media_root")

FACEBOOK_APP_ID = '531963513646710'
FACEBOOK_API_SECRET = '8f06287f20dc6dd922efb27b977a0d1b'

#GOOGLE_OAUTH2_KEY = 'AIzaSyBSMmC31JL-cWJP1BBwmXbj_9yM-6sSfCQ'
#GOOGLE_OAUTH2_SECRET = ''

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GooglePlusAuth',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL ='/'