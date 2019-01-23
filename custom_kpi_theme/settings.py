"""
Django settings for custom_kpi_theme project.

Generated by 'django-admin startproject' using Django 1.8.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
import importlib

try:
    from custom_kobocat_theme.local_settings import *

except ImportError:
    # Load from current settings file
    settings_file = 'kobo.settings'
    if settings_file not in sys.modules:
        current_settings = importlib.import_module(settings_file)
        sys.modules[settings_file] = current_settings
    else:
        current_settings = sys.modules[settings_file]

    locals().update(
    {
        k: getattr(current_settings, k)
        for k in dir(current_settings) if not k.startswith('_')
    })


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# Application definition
INSTALLED_APPS = list(INSTALLED_APPS) + \
                 ['custom_kpi_theme', 'snowpenguin.django.recaptcha2',]

ROOT_URLCONF = 'custom_kpi_theme.urls'

RECAPTCHA_PRIVATE_KEY = '6LdvRXUUAAAAAKGKUgTxAcGjC1ESPCtwNhsEX-r7'
RECAPTCHA_PUBLIC_KEY = '6LdvRXUUAAAAABu0RDupGcVLdehnyQJAT0eGIvby'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

# Defines the directory that contains the settings file as the _LOCAL_ROOT
# It is used for relative settings elsewhere.
_LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))

# Additional directories which hold static files
# STATICFILES_DIRS.append(
#     os.path.join(_LOCAL_ROOT, "static"),
# )
# STATICFILES_DIRS = STATICFILES_DIRS + (
#     os.path.join(_LOCAL_ROOT, 'jsapp'),
#     os.path.join(_LOCAL_ROOT, "static"),
#     ('mocha', os.path.join(BASE_DIR, 'node_modules', 'mocha'),),
# )

_LOCALE_DIR = os.path.join(_LOCAL_ROOT, 'locale')
_TEMPLATE_DIR = os.path.join(_LOCAL_ROOT, 'templates')

# Prioritize custom translations
LOCALE_PATHS = list(LOCALE_PATHS)
LOCALE_PATHS.insert(0, _LOCALE_DIR)

# Prioritize custom theme
template_dirs = list(TEMPLATES[0]['DIRS'])
template_dirs.insert(0, _TEMPLATE_DIR)

TEMPLATES[0]['DIRS'] = template_dirs

# WEBPACK_LOADER = {
#     'DEFAULT': {
#         # 'BUNDLE_DIR_NAME': 'jsapp/compiled/',
#         'BUNDLE_DIR_NAME': 'compiled/',
#         'POLL_INTERVAL': 0.5,
#         'TIMEOUT': 5,
#     }
# }
