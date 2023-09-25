"""Настройки проекта."""
from pathlib import Path

from configurations import Configuration, values
from dotenv import load_dotenv

load_dotenv()


class Base(Configuration):
    """Базовый класс конфигурации."""

    BASE_DIR = Path(__file__).resolve().parent.parent
    SECRET_KEY = values.SecretValue()
    DEBUG = values.BooleanValue(False)
    ALLOWED_HOSTS = values.ListValue([])
    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",

        "rangefilter",

        "apps.coffee"
    ]
    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]
    ROOT_URLCONF = "project.urls"
    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]
    WSGI_APPLICATION = "project.wsgi.application"
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
    AUTH_PASSWORD_VALIDATORS = values.ListValue(
        [
            {
                "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
            },
            {
                "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
            },
            {
                "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
            },
            {
                "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
            },
        ]
    )
    LANGUAGE_CODE = "en-us"
    TIME_ZONE = "UTC"
    USE_I18N = True
    USE_TZ = True
    STATIC_URL = "static/"
    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


class Development(Base):
    """Конфигурация окружения Development."""

    DEBUG = values.BooleanValue(True)
    INSTALLED_APPS = Base.INSTALLED_APPS + ['django_extensions', ]


class Production(Base):
    """Конфигурация окружения Production."""


class Test(Base):
    """Конфигурация окружения Test."""

    SECRET_KEY = "testing"
