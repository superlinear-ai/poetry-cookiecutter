# syntax=docker/dockerfile:experimental
{%- if cookiecutter.with_fastapi_api|int or cookiecutter.with_streamlit_app|int or cookiecutter.with_typer_cli|int %}
ARG APP_BASE_IMAGE=ci
{%- endif %}

FROM python:3.8-slim AS dev

# Install development tools: compilers, curl, fish, git, ssh, and starship.
RUN apt-get update && \
    apt-get install --no-install-recommends --yes build-essential curl git fish ssh && \
    chsh --shell /usr/bin/fish && \
    sh -c "$(curl -fsSL https://starship.rs/install.sh)" -- "--yes" && \
    mkdir -p ~/.config/fish/completions/ && \
    echo "set fish_greeting" >> ~/.config/fish/config.fish && \
    echo "starship init fish | source" >> ~/.config/fish/config.fish && \
    rm -rf /var/lib/apt/lists/*

# Configure Python to print tracebacks on crash [1], and to not buffer stdout and stderr [2].
# [1] https://docs.python.org/3/using/cmdline.html#envvar-PYTHONFAULTHANDLER
# [2] https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUNBUFFERED
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1

# Set the working directory.
WORKDIR /app/

# Install base development environment with Poetry and Poe the Poet.
ENV PATH /root/.local/bin/:$PATH
RUN --mount=type=cache,target=/root/.cache \
    pip install --no-input --upgrade pip poethepoet && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python - && \
    poetry config virtualenvs.create false && \
    poetry completions fish > ~/.config/fish/completions/poetry.fish && \
    poe _fish_completion > ~/.config/fish/completions/poe.fish

# Let Poe the Poet know it doesn't need to activate the Python environment.
ENV POETRY_ACTIVE 1

# Enable Poetry to publish to {% if cookiecutter.private_package_repository_name %}and install from a private package repository{% else %}PyPI{% endif %} [1].
# [1] https://pythonspeed.com/articles/build-secrets-docker-compose/
{%- if cookiecutter.private_package_repository_name %}
ARG POETRY_HTTP_BASIC_{{ cookiecutter.private_package_repository_name|upper }}_USERNAME
ENV POETRY_HTTP_BASIC_{{ cookiecutter.private_package_repository_name|upper }}_USERNAME $POETRY_HTTP_BASIC_{{ cookiecutter.private_package_repository_name|upper }}_USERNAME
ARG POETRY_HTTP_BASIC_{{ cookiecutter.private_package_repository_name|upper }}_PASSWORD
ENV POETRY_HTTP_BASIC_{{ cookiecutter.private_package_repository_name|upper }}_PASSWORD $POETRY_HTTP_BASIC_{{ cookiecutter.private_package_repository_name|upper }}_PASSWORD
{%- else %}
ARG POETRY_PYPI_TOKEN_PYPI
ENV POETRY_PYPI_TOKEN_PYPI $POETRY_PYPI_TOKEN_PYPI
{%- endif %}

FROM dev as ci

# Install the Python environment.
# TODO: Replace `--no-dev` with `--without test` when Poetry 1.2.0 is released.
COPY poetry.lock pyproject.toml /app/
RUN --mount=type=cache,target=/root/.cache \
    {%- if cookiecutter.private_package_repository_name %}
    --mount=type=secret,id=poetry-http-basic-username \
    --mount=type=secret,id=poetry-http-basic-password \
    {%- endif %}
    mkdir -p src/{{ cookiecutter.package_name|slugify|replace("-", "_") }}/ && touch src/{{ cookiecutter.package_name|slugify|replace("-", "_") }}/__init__.py && touch README.md && \
    {%- if cookiecutter.private_package_repository_name %}
    POETRY_HTTP_BASIC_{{ cookiecutter.private_package_repository_name|upper }}_USERNAME=${POETRY_HTTP_BASIC_{{ cookiecutter.private_package_repository_name|upper }}_USERNAME:-$(cat /run/secrets/poetry-http-basic-username)} \
    POETRY_HTTP_BASIC_{{ cookiecutter.private_package_repository_name|upper }}_PASSWORD=${POETRY_HTTP_BASIC_{{ cookiecutter.private_package_repository_name|upper }}_PASSWORD:-$(cat /run/secrets/poetry-http-basic-password)} \
    {%- endif %}
    poetry install --no-dev --no-interaction
{%- if cookiecutter.with_fastapi_api|int or cookiecutter.with_streamlit_app|int or cookiecutter.with_typer_cli|int %}

FROM $APP_BASE_IMAGE AS app

# Copy the package source code to the working directory.
COPY . .

# Expose the application.
ARG PORT=8000
ENV PORT $PORT
EXPOSE $PORT
{%- if cookiecutter.with_fastapi_api|int or cookiecutter.with_streamlit_app|int %}
ENTRYPOINT ["/usr/local/bin/poe"]
CMD [{% if cookiecutter.with_fastapi_api|int %}"serve"{% else %}"streamlit"{% endif %}]
{%- else %}
ENTRYPOINT ["/usr/local/bin/{{ cookiecutter.package_name|slugify }}"]
CMD []
{%- endif %}

# The following variables are supplied as build args at build time so that they are available at
# run time as environment variables [1].
# [1] https://docs.docker.com/docker-hub/builds/advanced/
ARG SOURCE_BRANCH
ENV SOURCE_BRANCH $SOURCE_BRANCH
ARG SOURCE_COMMIT
ENV SOURCE_COMMIT $SOURCE_COMMIT
ARG SOURCE_TIMESTAMP
ENV SOURCE_TIMESTAMP $SOURCE_TIMESTAMP
{%- endif %}
