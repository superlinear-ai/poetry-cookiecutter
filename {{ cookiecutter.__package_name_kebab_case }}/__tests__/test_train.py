"""Test {{ cookiecutter.package_name }}/train/train.py CLI Functionality."""

from typer.testing import CliRunner

from {{ cookiecutter.__package_name_snake_case }}.train.train import train

runner = CliRunner()


