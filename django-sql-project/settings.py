"""
Django settings for django-sql-project project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv

import mimetypes
mimetypes.add_type("text/css", ".css", True)

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r+$45&sm1im6(9a@dgmt7en0*v5w4p$j_$3+ohx!bay6pj%2d5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: In production, allow only those domains which you trust.
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://*.azurewebsites.net']
CORS_ALLOW_ALL_ORIGINS: True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'customerapi'
]

CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



ROOT_URLCONF = 'django-sql-project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django-sql-project.wsgi.application'


# Database connection details
# https://github.com/microsoft/mssql-django
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': os.getenv("DB_NAME", "amc-demo-db"),
        'HOST': os.getenv("DB_SERVER", "amc-demo-sql-server.database.windows.net"),
        'PORT': '1433',
        'USER': os.getenv("DB_USER", "amiebarkes"),
        'PASSWORD': os.getenv("DB_PASSWORD", "Fab1o@Am1e"),
        'OPTIONS': {
	            'driver': 'ODBC Driver 17 for SQL Server',
	        },
    }

    #To connect Azure SQL DB using MSI (Managed Service Identity)
    # {
    #     'ENGINE': 'mssql',
    #     'HOST': 'xyz.database.windows.net',
    #     'NAME': 'mydb', 
    #     'PORT': '', 
    #     'Trusted_Connection': 'no', 
    #     'OPTIONS': { 
    #         'driver': 'ODBC Driver 17 for SQL Server', 
    #         'extra_params': "Authentication=ActiveDirectoryMsi;Encrypt=yes;TrustServerCertificate=no" }
    # }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

# set this to False if the backend does not support using time zones
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
