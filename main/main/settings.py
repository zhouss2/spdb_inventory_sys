"""
Django settings for djangodemo project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_ROOT)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ul*gfz_biz5*fk5!v9ca4^qr(rs^56o@y4w20-$i-f%=kzb!%r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'main.activities',
    'main.articles',
    'main.authentication',
    'main.core',
    'main.overview',
    'main.feeds',
    'main.messenger',
    'main.questions',
    'main.search',
    'main.equipments',
    'main.equipmentlist',
)

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'spdb_inventory',
        'USER':'inventory',
        'PASSWORD':'1234',
        'HOST':"127.0.0.1",
        'PORT':'5432',
    }
}

# if os.getenv('DATABASE_URL'):
#     import dj_database_url
#     DATABASES['default'] = dj_database_url.config()

CACHES = {
    # "default": {
    #     "BACKEND": "django_redis.cache.RedisCache",
    #     "LOCATION": '127.0.0.1:6379',
    #     "OPTIONS": {
    #         "CLIENT_CLASS": "django_redis.client.DefaultClient",
    #     }
    # }
    'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.'
    #             'CommonPasswordValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

USE_TZ = True
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True
USE_L10N = True

LANGUAGE_CODE = 'zh-Hans'

LANGUAGES = (
    ('en', 'English'),
    ('zh-Hans', 'Chinese')
)

LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 
# print(STATIC_ROOT)
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
# print(STATICFILES_DIRS)
LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/overview/'

ALLOWED_SIGNUP_DOMAINS = ['*']


MEDIA_ROOT = os.path.join(BASE_DIR, r'main\articles\media')
# print(MEDIA_ROOT)
MEDIA_URL = '/main/articles/media/'