"""Test package version."""

from importlib.metadata import version


def test_version() -> None:
    """Test the package version."""
    assert isinstance(version('{{ cookiecutter.package_name|slugify }}'), str)
