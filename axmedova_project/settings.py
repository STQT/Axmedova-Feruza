"""
Django settings for axmedova_project project.
"""

import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure-dev-key-change-in-production')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1').split(',')

# CSRF trusted origins (for production with HTTPS)
CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', default='http://localhost:8000,http://127.0.0.1:8000').split(',')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    
    # Third party apps
    'crispy_forms',
    'crispy_bootstrap5',
    'ckeditor',
    'ckeditor_uploader',
    'storages',
    
    # Local apps
    'core',
]

# Middleware configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# WhiteNoise только если не используется R2 для статики
# WhiteNoise не нужен, когда статика обслуживается через R2/S3
USE_R2_STORAGE = config('USE_R2_STORAGE', default=False, cast=bool)
USE_R2_FOR_STATIC = config('USE_R2_FOR_STATIC', default=True, cast=bool) if USE_R2_STORAGE else False

if not (USE_R2_STORAGE and USE_R2_FOR_STATIC):
    # Добавляем WhiteNoise только если статика не на R2
    MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

ROOT_URLCONF = 'axmedova_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'core.context_processors.site_context',  # Custom context processor
            ],
        },
    },
]

WSGI_APPLICATION = 'axmedova_project.wsgi.application'

# Database
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': config('DB_ENGINE', default='django.db.backends.postgresql'),
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST', default='localhost'),
            'PORT': config('DB_PORT', default='5432'),
        }
    }

# Password validation
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
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files (local or Cloudflare R2)
# USE_R2_STORAGE уже определен выше для middleware

if USE_R2_STORAGE:
    # Cloudflare R2 Storage Configuration
    AWS_ACCESS_KEY_ID = config('R2_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('R2_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('R2_BUCKET_NAME')
    AWS_S3_ENDPOINT_URL = config('R2_ENDPOINT_URL')
    
    # R2 specific settings
    AWS_S3_REGION_NAME = 'auto'  # Cloudflare R2 требует 'auto'
    AWS_S3_SIGNATURE_VERSION = 's3v4'  # Используем signature v4
    AWS_S3_ADDRESSING_STYLE = 'path'  # Path-style addressing для R2
    
    # S3 settings
    AWS_S3_CUSTOM_DOMAIN = config('R2_CUSTOM_DOMAIN', default=None)
    AWS_DEFAULT_ACL = None  # R2 не поддерживает ACL, используем bucket policy
    AWS_QUERYSTRING_AUTH = False  # Не добавлять query parameters к URL
    AWS_S3_FILE_OVERWRITE = False
    AWS_S3_VERIFY = True
    AWS_S3_USE_SSL = True
    
    # Object parameters теперь настроены в storage_backends.py для каждого типа отдельно
    
    # Media files on R2
    DEFAULT_FILE_STORAGE = 'core.storage_backends.MediaStorage'
    # URL для media - без bucket name, т.к. storage class добавляет location
    if AWS_S3_CUSTOM_DOMAIN:
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
    else:
        MEDIA_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/media/'
    
    # Static files - загрузка на R2 для экономии места
    if USE_R2_FOR_STATIC:
        STATICFILES_STORAGE = 'core.storage_backends.StaticStorage'
        # URL для static - без bucket name, т.к. storage class добавляет location
        if AWS_S3_CUSTOM_DOMAIN:
            STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
        else:
            STATIC_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/static/'
        # STATIC_ROOT не нужен при использовании R2, но Django может его проверять
        # Создаем пустую директорию, чтобы избежать предупреждений
        # Используем значение из переменной окружения, если оно задано, иначе BASE_DIR
        try:
            static_root_path = config('STATIC_ROOT', default=None)
            if static_root_path:
                STATIC_ROOT = Path(static_root_path)
            else:
                STATIC_ROOT = BASE_DIR / 'staticfiles'
        except Exception:
            # Если что-то пошло не так, используем BASE_DIR
            STATIC_ROOT = BASE_DIR / 'staticfiles'
        # Создаем директорию, если она не существует (чтобы избежать предупреждений)
        STATIC_ROOT.mkdir(parents=True, exist_ok=True)
    else:
        # Без сжатия, чтобы не превысить квоту диска
        STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
        STATIC_ROOT = config('STATIC_ROOT', default=BASE_DIR / 'staticfiles')
else:
    # Local storage (default)
    MEDIA_URL = '/media/'
    MEDIA_ROOT = config('MEDIA_ROOT', default=BASE_DIR / 'media')
    STATIC_ROOT = config('STATIC_ROOT', default=BASE_DIR / 'staticfiles')


# CKEditor Configuration
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Strike'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source'],
            ['Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Image', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar'],
            ['Blockquote', 'CodeSnippet'],
        ],
        'height': 400,
        'width': '100%',
        'extraPlugins': ','.join([
            'codesnippet',
        ]),
    },
    'simple': {
        'toolbar': 'Basic',
        'toolbar_Basic': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink'],
        ],
        'height': 200,
        'width': '100%',
    },
}

# Whitenoise configuration
# Use simple storage for tests
import sys
if 'test' in sys.argv:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
    if not USE_R2_STORAGE:
        STATIC_ROOT = config('STATIC_ROOT', default=BASE_DIR / 'staticfiles')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Email Configuration
EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = config('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='noreply@example.com')
ADMIN_EMAIL = config('ADMIN_EMAIL', default='admin@example.com')

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = config('TELEGRAM_BOT_TOKEN', default='')
TELEGRAM_CHAT_ID = config('TELEGRAM_CHAT_ID', default='')

# Security Settings for Production
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'

