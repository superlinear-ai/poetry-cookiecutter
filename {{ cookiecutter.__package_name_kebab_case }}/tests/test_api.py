"""Test {{ cookiecutter.package_name }} REST API."""

from fastapi.testclient import TestClient

from {{ cookiecutter.__package_name_snake_case }}.api import app

client = TestClient(app)


def test_read_root() -> None:
    """Test that reading the root is successful."""
    response = client.get("/")
    assert response.ok
