"""Test {{ cookiecutter.package_name }} REST API."""

from fastapi.testclient import TestClient

from {{ cookiecutter.package_name|slugify|replace("-", "_") }}.api import app

client = TestClient(app)


def test_read_root() -> None:
    """Test that reading the root is successful."""
    response = client.get("/")
    assert response.status_code == 200
