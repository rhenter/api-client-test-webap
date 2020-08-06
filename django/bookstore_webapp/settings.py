import os

from dj_database_url import parse as parse_db_url
from django_cache_url import parse as parse_cache_url
from prettyconf import config
from unipath import Path

from .logging import get_loggers, get_logging_config
from .utils import get_version

# Project Structure
BASE_DIR = Path(__file__).ancestor(3)
PROJECT_DIR = Path(__file__).ancestor(2)
FRONTEND_DIR = PROJECT_DIR.child("frontend")

# App version
APP_VERSION = get_version()

# Developer Info
DEVELOPER_NAME = config("DEVELOPER_NAME", default='Henter')
DEVELOPER_WEBSITE = config("DEVELOPER_WEBSITE", default='https://www.make .com.br')

# Debug & Development
DEBUG = config("DEBUG", default=False, cast=config.boolean)

# Database
default_dburl = 'sqlite:///{}/db.sqlite3'.format(PROJECT_DIR)
DATABASES = {
    'default': config(
        'DATABASE_URL',
        default=default_dburl,
        cast=parse_db_url),
}
DATABASES['default']['CONN_MAX_AGE'] = config(
    'CONN_MAX_AGE',
    cast=config.eval,
    default='500')  # always connected
DATABASES['default']['TEST'] = {
    'NAME': config(
        'TEST_DATABASE_NAME',
        default=None)
}

#  Security & Signup/Signin
ADMIN_USERNAME = config('ADMIN_USERNAME', default='admin')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=config.list)
SECRET_KEY = config(
    'SECRET_KEY',
    default='example-kn59*npHxq)G#p7VkwfZCb)RgtUWaJjfDBrEYJ6fEk9Sj$(d)Q#uZ6U##'
)

#  Media & Static
MEDIA_URL = "/media/"
MEDIA_ROOT = config('MEDIA_ROOT', default=FRONTEND_DIR.child("media"))

STATIC_URL = config('STATIC_URL', default='/static/')
STATIC_ROOT = config(
    'STATIC_ROOT', default=str(PROJECT_DIR.child('staticfiles'))
)

STATICFILES_DIRS = [
    FRONTEND_DIR.child("static"),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# SCSS Compiler


# Django Sass
SASS_PROCESSOR_ROOT = FRONTEND_DIR.child("static")

# Media Files
USE_S3_BACKEND = config('USE_S3_BACKEND', default=False)
ASSESTS_STORAGE_ROOT = config('ASSESTS_STORAGE_ROOT', default='assets/')
DOCUMENTS_STORAGE_ROOT = config('DOCUMENTS_STORAGE_ROOT', default='documents/')
IMAGES_STORAGE_ROOT = config('IMAGES_STORAGE_ROOT', default='images/')

# Storage
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# Backend Storage AWS S3
if USE_S3_BACKEND:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    AWS_ACCESS_KEY_ID = config('S3_AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('S3_AWS_SECRET_ACCESS_KEY')
    AWS_S3_REGION_NAME = config('S3_AWS_S3_REGION_NAME')
    AWS_S3_SIGNATURE_VERSION = config('S3_AWS_S3_SIGNATURE_VERSION')

AWS_DEFAULT_ACL = None
AWS_STORAGE_BUCKET_NAME = config('S3_AWS_STORAGE_BUCKET_NAME', default='supplai-media')
# AWS_LOCATION = config('S3_AWS_STORAGE_BUCKET_NAME', default='supplai-www')
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_QUERYSTRING_EXPIRE = '604700'
# AWS_QUERYSTRING_AUTH = False

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party libs
    'django_filters',
    'corsheaders',
    'django_stuff',
    'widget_tweaks',
    'django_api_client',
    # Local
    'apps.core',
    'apps.book',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

# To accept js and css files on head of base html
SECURE_CONTENT_TYPE_NOSNIFF = False

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'bookstore_webapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (
            FRONTEND_DIR.child("templates"),
        ),
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': config(
                "TEMPLATE_DEBUG",
                default=DEBUG,
                cast=config.boolean),
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookstore_webapp.wsgi.application'

AUTHENTICATION_BACKENDS = (
    'django_stuff.backends.auth.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend'
)

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGES = (
    ("en", "English"),
    ("pt-br", "Português (Brasil)"),
)
LANGUAGE_CODE = 'pt-br'
LOCALE_PATHS = (
    PROJECT_DIR.child("locale"),
)


DECIMAL_SEPARATOR = ','
USE_THOUSAND_SEPARATOR = True

CORS_ORIGIN_ALLOW_ALL = True

LOGIN_URL = "/login/"
LOGOUT_URL = "/logout/"
LOGIN_REDIRECT_URL = "/"

# Logging
LOGGING = get_logging_config(
    get_loggers(
        config("LOG_LEVEL", default="INFO"),
        config("LOGGERS", default="", cast=config.list)
    )
)

# EMAIL Authentication Settings
EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

EMAIL_ADMIN = config("EMAIL_ADMIN")
EMAIL_SAC = config("EMAIL_SAC")

EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=config.boolean)
EMAIL_HOST = config("EMAIL_HOST", default='localhost')
EMAIL_PORT = config("EMAIL_PORT", default=25, cast=int)
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default='')
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default='')
DEFAULT_FROM_EMAIL = EMAIL_ADMIN

# # Swagger configs

SWAGGER_SETTINGS = {
    'SUPPORTED_SUBMIT_METHODS': ['get', 'post', 'put', 'delete', 'patch'],  # default
    'JSON_EDITOR': True
}

# Django REST Framework

DATE_FORMAT = '%d/%m/%Y'
DATETIME_FORMAT = 'iso-8601'
DATE_INPUT_FORMATS = (
    '%m/%d/%Y', '%d/%m/%Y', '%Y-%m-%d',
    '%m-%d-%Y', '%d-%m-%Y',
)
DATETIME_INPUT_FORMATS = [
    '%Y-%m-%d',  # '2006-10-25'
    '%d/%m/%Y',  # '25/10/2006'
    '%Y-%m-%d %H:%M',  # '2006-10-25 14:30'
    '%d/%m/%Y %H:%M',  # '25/10/2006 14:30'
    '%m/%d/%Y %H:%M',  # '10/25/2006 14:30'
    'iso-8601',
]

CACHES = {
    'default': config('CACHE_URL', default='locmem://', cast=parse_cache_url)
}
APPEND_SLASH = False

CACHED_SERIALIZER_TIMEOUT = config('CACHED_SERIALIZER_TIMEOUT', default='120', cast=config.eval)


ENDPOINTS = [
    '/v1/agreement/landing/',
    '/v1/company/landing_company_create/',
    '/v1/core/terms_of_service/',
    '/v1/discount/discounts/',
    '/v1/discount/online_discounts/',
    '/v1/faq/faqs/',
    '/v1/field_of_activity/fields_of_activity/',
    '/v1/giftcard/giftcards/',
    '/v1/promocode/vinculate_promocode/',
    '/v1/promocode/validate_promocode/',
    '/v1/sale/sales/',
    '/v1/sale/usage/',
    '/v1/store/stores/',
    '/v1/user/users/',
    '/v1/user/toggle_preference/',
    '/v1/virtual_card/virtual_cards/',
]

DJANGO_API_CLIENT = {
    'API': {
        'NAME': 'bookstore_api',
        'BASE_URL': config('BOOKSTORE_API_BASE_URL', default='http://localhost:9000'),
        'ENDPOINTS': [
            '/v1/book/books/'
        ],
        'AUTHENTICATION_ACCESS_TOKEN_TYPE': 'Token',
        'AUTHENTICATION_ACCESS_TOKEN': config('BOOKSTORE_API_ACCESS_TOKEN'),
        'LOCALE': 'pt-br',
        'TIMEOUT': config('BOOKSTORE_API_TIMEOUT', default=3, cast=int),
    },
    'SLUG_FIELD': 'id'
}
