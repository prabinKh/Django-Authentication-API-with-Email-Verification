"""
Django settings for djangoauthapi project.
Fixed & Optimized for macOS + Python 3.13 + Gmail SMTP (November 2025)
"""

from pathlib import Path
from datetime import timedelta
import os
from dotenv import load_dotenv

# ==================== CRITICAL SSL FIX FOR MACOS + PYTHON 3.13 ====================
import ssl
from django.core.mail.backends.smtp import EmailBackend

# Custom Email Backend that fixes certificate verification issues
class PatchedEmailBackend(EmailBackend):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Prefer certifi (secure), fall back to unverified only if certifi missing
        try:
            import certifi
            self.ssl_context = ssl.create_default_context(cafile=certifi.where())
        except ImportError:
            self.ssl_context = ssl._create_unverified_context()

# Load environment variables
load_dotenv()

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!)$*rly$1%dvcya%f!kx(4hgori2pi-c^90*g#pxo63d(p7!_3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'account',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoauthapi.urls'

# Custom User Model
AUTH_USER_MODEL = 'account.MyUser'

# CORS Settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:9000",
    "http://localhost:3000",  # Add if using React
]

# REST Framework & JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    "AUTH_HEADER_TYPES": ("Bearer",),
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoauthapi.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==================== EMAIL CONFIGURATION (GMAIL - WORKING 2025) ====================
EMAIL_BACKEND = 'djangoauthapi.settings.PatchedEmailBackend'  # Our fixed backend
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Console backend for development
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = os.getenv('EMAIL_USER', 'example@gmail.com')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD', 'aaaa aaaa aaaa aaaa')  # Your App Password
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_FROM', 'example@gmail.com')
EMAIL_TIMEOUT = 30

# Optional: Fallback to console during development if needed
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Password Reset Timeout (in seconds) - used in token generation
PASSWORD_RESET_TIMEOUT = 120  # 2 minutes
