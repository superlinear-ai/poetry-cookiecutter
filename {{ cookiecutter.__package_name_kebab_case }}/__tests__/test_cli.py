"""Test {{ cookiecutter.package_name }} CLI."""

from typer.testing import CliRunner

from {{ cookiecutter.__package_name_snake_case }}cli import app

runner = CliRunner()


def test_express() -> None:
    """Test that the say command works as expected."""
    message = "Hello world"
    result = runner.invoke(app, ["--message", message])
    assert result.exit_code == 0
    assert message in result.stdout
