from __future__ import annotations

import os


def _configure_pylint_django():
    os.environ["DJANGO_SETTINGS_MODULE"] = "project.settings"
    os.environ["DJANGO_CONFIGURATION"] = "Development"

    from configurations import importer  # type: ignore[import]

    importer.install()


if __name__ == "<run_path>":
    _configure_pylint_django()
