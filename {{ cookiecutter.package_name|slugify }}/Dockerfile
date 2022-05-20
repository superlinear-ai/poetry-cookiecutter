# syntax=docker/dockerfile:experimental
{%- if cookiecutter.with_fastapi_api|int or cookiecutter.with_streamlit_app|int or cookiecutter.with_typer_cli|int %}
ARG APP_BASE_IMAGE=ci
{%- endif %}

FROM python:{{ cookiecutter.python_version }}-slim AS base

# Install development tools: compilers, curl, git, ssh, starship, vim, and zsh.
RUN apt-get update && \
    apt-get install --no-install-recommends --yes build-essential curl git ssh vim zsh zsh-antigen && \
    chsh --shell /usr/bin/zsh && \
    sh -c "$(curl -fsSL https://starship.rs/install.sh)" -- "--yes" && \
    echo 'source /usr/share/zsh-antigen/antigen.zsh' >> ~/.zshrc && \
    echo 'antigen bundle zsh-users/zsh-autosuggestions' >> ~/.zshrc && \
    echo 'antigen apply' >> ~/.zshrc && \
    echo 'eval "$(starship init zsh)"' >> ~/.zshrc && \
    rm -rf /var/lib/apt/lists/*

# Configure Python to print tracebacks on crash [1], and to not buffer stdout and stderr [2].
# [1] https://docs.python.org/3/using/cmdline.html#envvar-PYTHONFAULTHANDLER
# [2] https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUNBUFFERED
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1

# Install Poetry.
ENV POETRY_VERSION 1.1.13
ENV PATH /root/.local/bin:$PATH
RUN --mount=type=cache,target=/root/.cache/ \
    curl -sSL https://install.python-poetry.org | python - --version $POETRY_VERSION

# Create and activate a virtual environment.
RUN python -m venv /opt/app-env
ENV PATH=/opt/app-env/bin:$PATH
ENV VIRTUAL_ENV=/opt/app-env

# Set the working directory.
WORKDIR /app/

FROM base as dev

# Install the development Python environment.
COPY .pre-commit-config.yaml poetry.lock* pyproject.toml /app/
RUN --mount=type=cache,target=/root/.cache/ \
    {%- if cookiecutter.private_package_repository_name %}
    --mount=type=secret,id=poetry_auth,target=/root/.config/pypoetry/auth.toml \
    {%- endif %}
    mkdir -p src/{{ cookiecutter.package_name|slugify|replace("-", "_") }}/ && touch src/{{ cookiecutter.package_name|slugify|replace("-", "_") }}/__init__.py && touch README.md && \
    poetry install --no-interaction && \
    mkdir -p /var/lib/poetry/ && cp poetry.lock /var/lib/poetry/ && \
    git init && pre-commit install --install-hooks && \
    mkdir -p /var/lib/git/ && cp .git/hooks/commit-msg .git/hooks/pre-commit /var/lib/git/

FROM base as ci

# Install the run time Python environment.
# TODO: Replace `--no-dev` with `--without test` when Poetry 1.2.0 is released.
COPY poetry.lock pyproject.toml /app/
RUN --mount=type=cache,target=/root/.cache/ \
    {%- if cookiecutter.private_package_repository_name %}
    --mount=type=secret,id=poetry_auth,target=/root/.config/pypoetry/auth.toml \
    {%- endif %}
    mkdir -p src/{{ cookiecutter.package_name|slugify|replace("-", "_") }}/ && touch src/{{ cookiecutter.package_name|slugify|replace("-", "_") }}/__init__.py && touch README.md && \
    poetry install --no-dev --no-interaction
{%- if cookiecutter.with_fastapi_api|int or cookiecutter.with_streamlit_app|int or cookiecutter.with_typer_cli|int %}

FROM $APP_BASE_IMAGE AS app

# Copy the package source code to the working directory.
COPY . .

# Expose the application.
{%- if cookiecutter.with_fastapi_api|int or cookiecutter.with_streamlit_app|int %}
ENTRYPOINT ["/opt/app-env/bin/poe"]
CMD [{% if cookiecutter.with_fastapi_api|int %}"serve"{% else %}"streamlit"{% endif %}]
{%- else %}
ENTRYPOINT ["/opt/app-env/bin/{{ cookiecutter.package_name|slugify }}"]
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
