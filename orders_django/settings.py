"""
Django settings for orders_django project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-lnnsidc($p&z5*tn57i+_#jbp(34tl+an55h%n#cii0n1v35j3"
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_celery_results',
    'product',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'orders_django.urls'

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

WSGI_APPLICATION = 'orders_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
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

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", 'django-db')

CELERY_BEAT_SCHEDULE = {
      'add-every-30-seconds': {
        'task': 'product.tasks.create_update_delete_product',
        'schedule': 30.0
    },
}

SERVICE_ACCOUNT = {
    "type": "service_account",
    "project_id": "testsheet-354509",
    "private_key_id": "4cbe1a851ced821a4993d7a3ea6439fc225dc9b3",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC/AjhXdHlmN0ge\nTnI2/7QnPxmv/zGUr+V08z/NfSetnsMYLzYIIMyFeLH9ohMJkRLCpikGhEvXAH+W\n0YfAUNVphQd3URZCXn/zQVYZQZRwTNxbJQTBTWMtDijG06C6fkbVIJupWvEWDEwa\nbCqMClSewsgwjClMv8ZQJjWNKQ55AQ1MpRksp5TZ2fAo9Te6wOSntLxA0wwq7T8U\nQ0flNxjUZbCuE4Qm1NoEGgSuWGd/pcis4ZPDzf658rDAvY1TfvteVd2Rz06RoDXj\nRs8rBOOeGj0QepdtNo7tnOe3fvMCB+E9CpF1ztXtMenAnRh1HeLuH8tCjIoXcCHW\nxfZNelXpAgMBAAECggEAS8sgO0fLIm3eTrRXKw7VWFt4IHfVn0ga94jMsQgwNftR\nNCgLuzb0oSPvERN+lWW9OYMAtYbKp1KZzmlvgjcxMBFrEIQbHpPsFsU+2n/E3LkL\nGZm7ZM8GAytir97rIQWZqtmpGw8sqlCP5E42peI1iNgG4wjDHKLemRBIYK7BgO7j\nW2ZJvoHSdi0ma289AJz+mWfvT+TMlCQNZNMTzcBYVMH3NydnysMwP74f7UHYEi62\nCDQ8PWZCpCIxa521SoXoECScrduZjIMvrFo0H3tlrKOkhlOyRiT89JKi04L3YNkA\nJQ0AmiGF3Ua0SFfT4KZhaYmApx8Hk9H7WwV7CdRaDwKBgQDvzwoVutiWxD06P5RM\nwWq468VysIGlJcQxmo93BsEVqvsMZmweMQ95Eyrg3EL+YnuEuZDSaImlcUpuMn72\nVS3/5IEp+REv20GZiUPqHif6RPrlsTYurYY4HMxRRS2d4bVNc3sXS9AwG5EjWIQN\nL5Q2Gze/BjENXJmNCXfwnR2wpwKBgQDL57LVrnZQAHsSjGZXssJy1//0xgVuWsXg\n0ajS37q6Y3MJ+lKWU8Wxjg/AbRw+e+HJTdL6aBB0kVUvcfxeokMx4jNuy/aqTNqE\nKM/VchCRFfkPnnbHwWdu1al/dEshwHtcgeiwBkn+imA/HnzZ1HsjxAIeMe+FOgwx\n/LXkL72G7wKBgQDR6eKDCO5EcvzBexv+YCRiQIeykAy8GiX14byJTRFBPUzKGvGz\nL/DCY+PZtxSxhlVm5eR+OeGbP2MOuQbn68H7R/NEYXAI+x0eH8iiK8mEylLxMsEh\n9OUTQyoaTbrTg9pnNJnf144iPk86qGXXAPn0rriKbwoLDy6eBVbG+VEe6wKBgAa2\nCIfJ5zD44xQYNOIcCxRWkaEPx2v7ZtngbKsMHAw4a7ffWkqCVVZjs5cEwFI6J5NF\nkXUWabw8cE5QdRr0QjvpEwJJikPOpb6FzVlcGLl9vKXL9GLctbfLJnoAbNyehjDk\nQbFRc6wCB+rr6PYObUMfF2bBA/4hi/c1NxNckuNXAoGBAMSEUZ0Vg+8UgKmjmqIa\n0erU69ri3ppM6zrW0EVL1dKvyPWoFE5rlRoSQ0QJsA/db/YdxlctdO8qJz+Cur1s\n/KFTzbXBs3J81cxEMqpqIFtjwDnEZ6IE5nH6ikKB3i03ne3gayg8DnTRtQvXfhLG\nCAQ3UCQ0M5IqmWeGPU5uTiXb\n-----END PRIVATE KEY-----\n",
    "client_email": "account@testsheet-354509.iam.gserviceaccount.com",
    "client_id": "113922432150408444260",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/account%40testsheet-354509.iam.gserviceaccount.com"
}

REST_FRAMEWORK = {
        "DEFAULT_PAGINATION_CLASS":
        "rest_framework.pagination.PageNumberPagination",
        "PAGE_SIZE": 40,
    }

TELEGRAM_BOT_URL = ""
TELEGRAM_CHAT_ID = ""