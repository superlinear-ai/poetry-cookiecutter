import os
import shutil

# Read Cookiecutter configuration.
package_name = "{{ cookiecutter.__package_name_snake_case }}"
with_fastapi_api = int("{{ cookiecutter.with_fastapi_api }}")
with_sentry_logging = int("{{ cookiecutter.with_sentry_logging }}")
with_streamlit_app = int("{{ cookiecutter.with_streamlit_app }}")
with_typer_cli = int("{{ cookiecutter.with_typer_cli }}")
continuous_integration = "{{ cookiecutter.continuous_integration }}"
is_deployable_app = "{{ not not cookiecutter.with_fastapi_api|int or not not cookiecutter.with_streamlit_app|int }}" == "True"
is_publishable_package = "{{ not cookiecutter.with_fastapi_api|int and not cookiecutter.with_streamlit_app|int }}" == "True"

# Remove FastAPI if not selected.
if not with_fastapi_api:
    os.remove(f"src/{package_name}/api.py")
    os.remove("tests/test_api.py")

# Remove Sentry if not selected.
if not with_sentry_logging:
    os.remove(f"src/{package_name}/sentry.py")
    os.remove("tests/test_sentry.py")

# Remove Streamlit if not selected.
if not with_streamlit_app:
    os.remove("streamlit_app.py")

# Remove Typer if not selected.
if not with_typer_cli:
    os.remove(f"src/{package_name}/cli.py")
    os.remove("tests/test_cli.py")

# Remove the continuous integration provider that is not selected.
if continuous_integration != "GitHub":
    shutil.rmtree(".github/")
elif continuous_integration != "GitLab":
    os.remove(".gitlab-ci.yml")

# Remove unused GitHub Actions workflows.
if continuous_integration == "GitHub":
    if not is_deployable_app:
        os.remove(".github/workflows/deploy.yml")
    if not is_publishable_package:
        os.remove(".github/workflows/publish.yml")
