# syntax=docker/dockerfile:1
ARG PYTHON_VERSION={{ cookiecutter.python_version }}
FROM python:$PYTHON_VERSION-slim AS base
{%- if cookiecutter.development_environment == "strict" %}

# Configure Python to print tracebacks on crash [1], and to not buffer stdout and stderr [2].
# [1] https://docs.python.org/3/using/cmdline.html#envvar-PYTHONFAULTHANDLER
# [2] https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUNBUFFERED
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1
{%- endif %}

# Install Poetry.
ENV POETRY_VERSION 1.3.1
RUN --mount=type=cache,target=/root/.cache/pip/ \
    pip install poetry~=$POETRY_VERSION

# Install compilers that may be required for certain packages or platforms.
RUN rm /etc/apt/apt.conf.d/docker-clean
RUN --mount=type=cache,target=/var/cache/apt/ \
    --mount=type=cache,target=/var/lib/apt/ \
    apt-get update && \
    apt-get install --no-install-recommends --yes build-essential

# Create a non-root user and switch to it [1].
# [1] https://code.visualstudio.com/remote/advancedcontainers/add-nonroot-user
ARG UID=1000
ARG GID=$UID
RUN groupadd --gid $GID app && \
    useradd --create-home --gid $GID --uid $UID app && \
    chown app /opt/
USER app

# Create and activate a virtual environment.
RUN python -m venv /opt/{{ cookiecutter.__package_name_kebab_case }}-env
ENV PATH /opt/{{ cookiecutter.__package_name_kebab_case }}-env/bin:$PATH
ENV VIRTUAL_ENV /opt/{{ cookiecutter.__package_name_kebab_case }}-env

# Set the working directory.
WORKDIR /workspaces/{{ cookiecutter.__package_name_kebab_case }}/

# Install the run time Python dependencies in the virtual environment.
COPY --chown=app:app poetry.lock* pyproject.toml /workspaces/{{ cookiecutter.__package_name_kebab_case }}/
RUN mkdir -p /home/app/.cache/pypoetry/ && mkdir -p /home/app/.config/pypoetry/ && \
    mkdir -p src/{{ cookiecutter.__package_name_snake_case }}/ && touch src/{{ cookiecutter.__package_name_snake_case }}/__init__.py && touch README.md
RUN --mount=type=cache,uid=$UID,gid=$GID,target=/home/app/.cache/pypoetry/ \
    {%- if cookiecutter.private_package_repository_name %}
    --mount=type=secret,id=poetry-auth,uid=$UID,gid=$GID,target=/home/app/.config/pypoetry/auth.toml \
    {%- endif %}
    poetry install --only main --no-interaction



FROM base as ci

# Allow CI to run as root.
USER root

# Install git so we can run pre-commit.
RUN --mount=type=cache,target=/var/cache/apt/ \
    --mount=type=cache,target=/var/lib/apt/ \
    apt-get update && \
    apt-get install --no-install-recommends --yes git

# Install the CI/CD Python dependencies in the virtual environment.
RUN --mount=type=cache,target=/root/.cache/pypoetry/ \
    {%- if cookiecutter.private_package_repository_name %}
    --mount=type=secret,id=poetry-auth,target=/root/.config/pypoetry/auth.toml \
    {%- endif %}
    poetry install --only main,test --no-interaction



FROM base as dev

# Install development tools: compilers, curl, git, gpg, ssh, starship, sudo, vim, and zsh.
USER root
RUN --mount=type=cache,target=/var/cache/apt/ \
    --mount=type=cache,target=/var/lib/apt/ \
    apt-get update && \
    apt-get install --no-install-recommends --yes build-essential curl git gnupg ssh sudo vim zsh zsh-antigen && \
    sh -c "$(curl -fsSL https://starship.rs/install.sh)" -- "--yes" && \
    usermod --shell /usr/bin/zsh app && \
    echo 'app ALL=(root) NOPASSWD:ALL' > /etc/sudoers.d/app && chmod 0440 /etc/sudoers.d/app
USER app

# Install the development Python dependencies in the virtual environment.
RUN --mount=type=cache,uid=$UID,gid=$GID,target=/home/app/.cache/pypoetry/ \
    {%- if cookiecutter.private_package_repository_name %}
    --mount=type=secret,id=poetry-auth,uid=$UID,gid=$GID,target=/home/app/.config/pypoetry/auth.toml \
    {%- endif %}
    poetry install --no-interaction

# Persist output generated during docker build so that we can restore it in the dev container.
COPY --chown=app:app .pre-commit-config.yaml /workspaces/{{ cookiecutter.__package_name_kebab_case }}/
RUN mkdir -p /opt/build/poetry/ && cp poetry.lock /opt/build/poetry/ && \
    git init && pre-commit install --install-hooks && \
    mkdir -p /opt/build/git/ && cp .git/hooks/commit-msg .git/hooks/pre-commit /opt/build/git/

# Configure the non-root user's shell.
RUN echo 'source /usr/share/zsh-antigen/antigen.zsh' >> ~/.zshrc && \
    echo 'antigen bundle zsh-users/zsh-syntax-highlighting' >> ~/.zshrc && \
    echo 'antigen bundle zsh-users/zsh-autosuggestions' >> ~/.zshrc && \
    echo 'antigen apply' >> ~/.zshrc && \
    echo 'eval "$(starship init zsh)"' >> ~/.zshrc && \
    echo 'HISTFILE=~/.history/.zsh_history' >> ~/.zshrc && \
    echo 'HISTSIZE=1000' >> ~/.zshrc && \
    echo 'SAVEHIST=1000' >> ~/.zshrc && \
    echo 'setopt share_history' >> ~/.zshrc && \
    zsh -c 'source ~/.zshrc'
{%- if cookiecutter.private_package_repository_name %}

# Enable Poetry to read the private package repository credentials.
RUN ln -s /run/secrets/poetry-auth /home/app/.config/pypoetry/auth.toml
{%- endif %}
{%- if cookiecutter.with_fastapi_api|int or cookiecutter.with_streamlit_app|int or cookiecutter.with_typer_cli|int %}



FROM base AS app

# Copy the package source code to the working directory.
COPY --chown=app:app . .

# Expose the application.
{%- if cookiecutter.with_fastapi_api|int or cookiecutter.with_streamlit_app|int %}
ENTRYPOINT ["/opt/{{ cookiecutter.__package_name_kebab_case }}-env/bin/poe"]
CMD [{% if cookiecutter.with_fastapi_api|int %}"serve"{% else %}"streamlit"{% endif %}]
{%- else %}
ENTRYPOINT ["/opt/{{ cookiecutter.__package_name_kebab_case }}-env/bin/{{ cookiecutter.__package_name_kebab_case }}"]
CMD []
{%- endif %}
{%- endif %}
