#-*- coding:utf-8 -*-

"""
Author: Wang, Jun
Email: wangjun41@baidu.com
Date: 2018-11-16 
"""
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j7peoaq9os*6^31afc^7c@4gzus1(=!ri0&!-+utu%4=kxa5gn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
LOGGING_CONFIG = None
"""
[logger_root]
level=INFO

[handler_consoleHandler]
level=INFO

[handler_fileHandler]
level=INFO
path=/var/log/eam/
mode=a
maxbytes=8388608
backupcount=10

[formatter_simpleFormatter]
format=%(thread)d: %(asctime)s - %(levelname)s - %(message)s
datefmt=%Y-%m-%d %H:%M:%S
"""
EAM_LOGGING = {
    "logger_root": {
        "level": "INFO"
    },
    "handler_consoleHandler": {
        "level": "INFO"
    },
    "handler_fileHandler": {
        "level": "INFO",
        "path": "/var/log/eam/",
        "mode": "a",
        "maxbytes": 8388608,
        "backupcount": 5
    },
    "formatter_simpleFormatter": {
        "format": '%(asctime)-15s %(levelname)s %(filename)s:%(lineno)d %(message)s',
        "datefmt": "%Y-%m-%d %H:%M:%S"
    }
}

ALLOWED_HOSTS = ["*"]

TIME_ZONE = 'Asia/Shanghai'

FILE_UPLOAD_HANDLERS = ("django_excel.ExcelMemoryFileUploadHandler",
                        "django_excel.TemporaryExcelFileUploadHandler")
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'upload'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': [ BASE_DIR + "/templates"],
        'DIRS': [BASE_DIR + "/static"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'activflow.core.processors.global_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

#DB_NAME = 'eam'
#DB_USER = 'root'
#DB_PASSWORD = '123456'
#DB_HOST = 'localhost'
#DB_PORT = '3306'

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': DB_NAME,
#        'USER': DB_USER,
#        'PASSWORD': DB_PASSWORD,
#        'HOST': DB_HOST,                      # Empty for localhost
#        'PORT': DB_PORT,
#    }
#}

SQLITE_DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
     }
 }

#DATABASES = SQLITE_DATABASES
# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_I18N = True

USE_L10N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT= os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

DEFAULT_CHARSET='utf-8'