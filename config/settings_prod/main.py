from dotenv import load_dotenv

from pathlib import Path

import os


load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.getenv('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = os.getenv('DEBUG', False)

ALLOWED_HOSTS = [os.getenv('ALLOWED_HOSTS', '*')]

'''
CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True
'''

# Data for Request

DATA_UPLOAD_MAX_MEMORY_SIZE = 1572864

DATA_UPLOAD_MAX_NUMBER_FIELDS = 500

DATA_UPLOAD_MAX_NUMBER_FILES = 50


# Sessions

SESSION_COOKIE_AGE = 1814400
