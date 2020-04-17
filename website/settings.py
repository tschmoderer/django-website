"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import yaml 

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECURITY WARNING: don't run with debug turned on in production!

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader = yaml.FullLoader)
    
SECRET_KEY = cfg['key']
DEBUG      = cfg['dbg']

ALLOWED_HOSTS = ['www.iathena.fr', 'iathena.fr', 'localhost', '127.0.0.1']

ADMINS   = (('Timothee Schmoderer', 'webmaster@iathena.fr'),)
MANAGERS = ADMINS

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.forms', # for markdownx widget
    'markdownx',
    'sass_processor',
    'widget_tweaks',
    'crispy_forms',
    'homepage',
    'blog',
    'music',
]

# Custom widget in forms 
FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # personnal addons: 
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                # 'homepage.context_processors.add_login_form',
            ],
        },
    },
]

TEMPLATE_STRING_IF_INVALID = 'Variable not defined'

WSGI_APPLICATION = 'website.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST':'',
        'PORT':'',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N  = True
USE_L10N  = True
USE_TZ    = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL  = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets/'),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]


# Media settings

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL  = '/media/'

# Misc settings 

APPEND_SLASH = True
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True 

# Sass settings

SASS_PROCESSOR_ROOT = STATIC_ROOT

SASS_PROCESSOR_INCLUDE_DIRS = [
    os.path.join(BASE_DIR, 'assets/sass/'),
]

# Login Settings 
# TODO: change for data base pseudo instead
# LOGOUT_REDIRECT_URL = '/tschmoderer/'
# LOGIN_REDIRECT_URL = '/tschmoderer/'
# LOGIN_URL = '/'