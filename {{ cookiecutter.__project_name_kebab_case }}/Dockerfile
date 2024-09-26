# syntax=docker/dockerfile:1
ARG PYTHON_VERSION={{ cookiecutter.python_version }}
FROM {{ cookiecutter.__docker_image }} AS base

# Remove docker-clean so we can keep the apt cache in Docker build cache.
RUN rm /etc/apt/apt.conf.d/docker-clean
{%- if cookiecutter.development_environment == "strict" %}

# Configure Python to print tracebacks on crash [1], and to not buffer stdout and stderr [2].
# [1] https://docs.python.org/3/using/cmdline.html#envvar-PYTHONFAULTHANDLER
# [2] https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUNBUFFERED
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1
{%- endif %}

# Create a non-root user and switch to it [1].
# [1] https://code.visualstudio.com/remote/advancedcontainers/add-nonroot-user
ARG UID=1000
ARG GID=$UID
RUN groupadd --gid $GID user && \
    useradd --create-home --gid $GID --uid $UID user --no-log-init && \
    chown user /opt/
USER user

# Create and activate a virtual environment.
ENV VIRTUAL_ENV /opt/{{ cookiecutter.__project_name_kebab_case }}-env
ENV PATH $VIRTUAL_ENV/bin:$PATH
RUN python -m venv $VIRTUAL_ENV

# Set the working directory.
WORKDIR /workspaces/{{ cookiecutter.__project_name_kebab_case }}/



FROM base as poetry

USER root

# Install Poetry in separate venv so it doesn't pollute the main venv.
ENV POETRY_VERSION 1.8.0
ENV POETRY_VIRTUAL_ENV /opt/poetry-env
RUN --mount=type=cache,target=/root/.cache/pip/ \
    python -m venv $POETRY_VIRTUAL_ENV && \
    $POETRY_VIRTUAL_ENV/bin/pip install poetry~=$POETRY_VERSION && \
    ln -s $POETRY_VIRTUAL_ENV/bin/poetry /usr/local/bin/poetry

# Install compilers that may be required for certain packages or platforms.
RUN --mount=type=cache,target=/var/cache/apt/ \
    --mount=type=cache,target=/var/lib/apt/ \
    apt-get update && \
    apt-get install --no-install-recommends --yes build-essential

USER user

# Install the run time Python dependencies in the virtual environment.
COPY --chown=user:user poetry.lock* pyproject.toml /workspaces/{{ cookiecutter.__project_name_kebab_case }}/
RUN mkdir -p /home/user/.cache/pypoetry/ && mkdir -p /home/user/.config/pypoetry/ && \
    mkdir -p src/{{ cookiecutter.__project_name_snake_case }}/ && touch src/{{ cookiecutter.__project_name_snake_case }}/__init__.py && touch README.md
RUN --mount=type=cache,uid=$UID,gid=$GID,target=/home/user/.cache/pypoetry/ \
    poetry install --only main --all-extras --no-interaction



FROM poetry as dev

# Install development tools: curl, git, gpg, ssh, starship, sudo, vim, and zsh.
USER root
RUN --mount=type=cache,target=/var/cache/apt/ \
    --mount=type=cache,target=/var/lib/apt/ \
    apt-get update && \
    apt-get install --no-install-recommends --yes curl git gnupg ssh sudo vim zsh && \
    sh -c "$(curl -fsSL https://starship.rs/install.sh)" -- "--yes" && \
    usermod --shell /usr/bin/zsh user && \
    echo 'user ALL=(root) NOPASSWD:ALL' > /etc/sudoers.d/user && chmod 0440 /etc/sudoers.d/user
RUN git config --system --add safe.directory '*'
USER user

# Install the development Python dependencies in the virtual environment.
RUN --mount=type=cache,uid=$UID,gid=$GID,target=/home/user/.cache/pypoetry/ \
    poetry install --all-extras --no-interaction

# Persist output generated during docker build so that we can restore it in the dev container.
COPY --chown=user:user .pre-commit-config.yaml /workspaces/{{ cookiecutter.__project_name_kebab_case }}/
RUN mkdir -p /opt/build/poetry/ && cp poetry.lock /opt/build/poetry/ && \
    git init && pre-commit install --install-hooks && \
    mkdir -p /opt/build/git/ && cp .git/hooks/commit-msg .git/hooks/pre-commit /opt/build/git/

# Configure the non-root user's shell.
ENV ANTIDOTE_VERSION 1.8.6
RUN git clone --branch v$ANTIDOTE_VERSION --depth=1 https://github.com/mattmc3/antidote.git ~/.antidote/ && \
    echo 'zsh-users/zsh-syntax-highlighting' >> ~/.zsh_plugins.txt && \
    echo 'zsh-users/zsh-autosuggestions' >> ~/.zsh_plugins.txt && \
    echo 'source ~/.antidote/antidote.zsh' >> ~/.zshrc && \
    echo 'antidote load' >> ~/.zshrc && \
    echo 'eval "$(starship init zsh)"' >> ~/.zshrc && \
    echo 'HISTFILE=~/.history/.zsh_history' >> ~/.zshrc && \
    echo 'HISTSIZE=1000' >> ~/.zshrc && \
    echo 'SAVEHIST=1000' >> ~/.zshrc && \
    echo 'setopt share_history' >> ~/.zshrc && \
    echo 'bindkey "^[[A" history-beginning-search-backward' >> ~/.zshrc && \
    echo 'bindkey "^[[B" history-beginning-search-forward' >> ~/.zshrc && \
    mkdir ~/.history/ && \
    zsh -c 'source ~/.zshrc'

FROM base AS app

# Copy the virtual environment from the poetry stage.
COPY --from=poetry $VIRTUAL_ENV $VIRTUAL_ENV

# Copy the {{ cookiecutter.project_type }} source code to the working directory.
COPY --chown=user:user ./src ./src
COPY --chown=user:user ./pyproject.toml .
COPY --chown=user:user ./poetry.lock .

# Expose the app.
ENTRYPOINT ["/opt/{{ cookiecutter.__project_name_kebab_case }}-env/bin/poe"]
CMD ["api"]
