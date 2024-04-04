"""Test {{ cookiecutter.project_name }} CLI."""

from typer.testing import CliRunner

from {{ cookiecutter.__project_name_snake_case }}.cli import app

runner = CliRunner()


def test_fire() -> None:
    """Test that the fire command works as expected."""
    name = "GLaDOS"
    result = runner.invoke(app, ["--name", name])
    assert result.exit_code == 0
    assert name in result.stdout
