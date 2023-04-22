"""WSGI config for project."""
import os

configuration = os.getenv("ENVIRONMENT", "development").title()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", configuration)

from configurations.wsgi import get_wsgi_application  # pylint: disable=wrong-import-position

application = get_wsgi_application()
