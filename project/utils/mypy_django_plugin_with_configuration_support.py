"""Поддержка django-configuration для mypy."""
import os
from configurations.importer import install

from mypy_django_plugin import main


def plugin(version):
    """django-stubs с поддержкой django-configurations."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    os.environ.setdefault("DJANGO_CONFIGURATION", "Development")
    install()
    return main.plugin(version)
