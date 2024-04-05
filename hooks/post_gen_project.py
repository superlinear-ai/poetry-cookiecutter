import os
import shutil

# Read Cookiecutter configuration.
project_name = "{{ cookiecutter.__project_name_snake_case }}"
development_environment = "{{ cookiecutter.development_environment }}"
with_fastapi_api = int("{{ cookiecutter.with_fastapi_api }}")
with_typer_cli = int("{{ cookiecutter.with_typer_cli }}")
continuous_integration = "{{ cookiecutter.continuous_integration }}"
is_application = "{{ cookiecutter.project_type == 'app' }}" == "True"

# Remove py.typed and Dependabot if not in strict mode.
if development_environment != "strict":
    os.remove(f"src/{project_name}/py.typed")
    os.remove(".github/dependabot.yml")

# Remove FastAPI if not selected.
if not with_fastapi_api:
    os.remove(f"src/{project_name}/api.py")
    os.remove("tests/test_api.py")

# Remove Typer if not selected.
if not with_typer_cli:
    os.remove(f"src/{project_name}/cli.py")
    os.remove("tests/test_cli.py")

# Remove the continuous integration provider that is not selected.
if continuous_integration != "GitHub":
    shutil.rmtree(".github/")
elif continuous_integration != "GitLab":
    os.remove(".gitlab-ci.yml")

# Remove unused GitHub Actions workflows.
if continuous_integration == "GitHub":
    if is_application:
        os.remove(".github/workflows/publish.yml")
    else:
        os.remove(".github/workflows/deploy.yml")
