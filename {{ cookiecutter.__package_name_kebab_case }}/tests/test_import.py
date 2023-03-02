"""Test {{ cookiecutter.package_name }}."""

import {{ cookiecutter.__package_name_snake_case }}


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance({{ cookiecutter.__package_name_snake_case }}.__name__, str)
