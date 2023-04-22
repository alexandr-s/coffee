"""Тестирование версии."""
from project import __version__


def test_version():
    """Тестирование версии."""
    assert __version__ == "0.1.0"
