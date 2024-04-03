"""Test {{ cookiecutter.project_name }}."""

import {{ cookiecutter.__project_name_snake_case }}


def test_import() -> None:
    """Test that the {{ cookiecutter.project_type }} can be imported."""
    assert isinstance({{ cookiecutter.__project_name_snake_case }}.__name__, str)
