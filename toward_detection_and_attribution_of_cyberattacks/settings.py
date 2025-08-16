# toward_detection_and_attribution_of_cyberattacks/toward_detection_and_attribution_of_cyberattacks/settings.py

from pathlib import Path
import os

# =========================
# Base paths
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# Core settings
# =========================
SECRET_KEY = 'm+1edl5m-5@u9b8-=4-4mq&o1%agco2xpl8c!7sn7!eowjk#'  # keep/change as you want
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Silence AutoField warnings on older models
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =========================
# Apps / Middleware
# =========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Remote_User',
    'Service_Provider',
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

ROOT_URLCONF = 'toward_detection_and_attribution_of_cyberattacks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # your templates live under Template/htmls
        'DIRS': [BASE_DIR / 'Template' / 'htmls'],
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

WSGI_APPLICATION = 'toward_detection_and_attribution_of_cyberattacks.wsgi.application'

# =========================
# Database (MySQL, hardcoded creds)
# =========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'toward_detection_and_attribution_of_cyberattacks',
        'USER': 'root',
        'PASSWORD': 'vignan',          # <-- your MySQL password
        'HOST': '127.0.0.1',
        'PORT': '3306',
        # These help on many Windows/MySQL 8 setups; safe to keep.
        'OPTIONS': {
            'auth_plugin': 'mysql_native_password',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# =========================
# Password validation
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# =========================
# i18n / tz
# =========================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'  # change to 'Asia/Kolkata' if you prefer
USE_I18N = True
USE_L10N = True
USE_TZ = True

# =========================
# Static / Media
# =========================
STATIC_URL = '/static/'
# Where collectstatic will output files (safe locally too)
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Extra static assets you ship with the project (images/css under Template/images)
STATICFILES_DIRS = [
    BASE_DIR / 'Template' / 'images'
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'Template' / 'media'
