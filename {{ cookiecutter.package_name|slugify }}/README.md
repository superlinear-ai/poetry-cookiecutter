# {{ cookiecutter.package_name }}

{{ cookiecutter.package_description }}

{% if cookiecutter.with_fastapi_api|int or cookiecutter.with_streamlit_app|int -%}
## Usage

To serve this package, run `docker-compose up app`.
{%- else -%}
## Installing

To add and install this package as a dependency of your project, run `poetry add {{ cookiecutter.package_name|slugify }}`.
{%- endif %}

## Contributing

<details>
<summary>Setup: once per device</summary>

{% if cookiecutter.continuous_integration == "GitLab" -%}
1. [Generate an SSH key](https://docs.gitlab.com/ee/ssh/README.html#generate-an-ssh-key-pair) for GitLab, [add the SSH key to your GitLab account](https://docs.gitlab.com/ee/ssh/README.html#add-an-ssh-key-to-your-gitlab-account), and [add the SSH key to your authentication agent](https://docs.gitlab.com/ee/ssh/README.html#configure-ssh-to-point-to-a-different-directory).
{%- if cookiecutter.private_package_repository_name %}
1. [Create a personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token) with the `api` scope and use it to [configure Poetry's credentials for this package's private repository](https://python-poetry.org/docs/repositories/#configuring-credentials):
    ```bash
    # bash
    echo "export POETRY_HTTP_BASIC_{{ cookiecutter.private_package_repository_name|upper }}_USERNAME='{personal access token name}'" >> ~/.bash_profile
    echo "export POETRY_HTTP_BASIC_{{ cookiecutter.private_package_repository_name|upper }}_PASSWORD='{personal access token}'" >> ~/.bash_profile
    
    # fish
    echo "set --export POETRY_HTTP_BASIC_{{ cookiecutter.private_package_repository_name|upper }}_USERNAME '{personal access token name}'" >> ~/.config/fish/config.fish
    echo "set --export POETRY_HTTP_BASIC_{{ cookiecutter.private_package_repository_name|upper }}_PASSWORD '{personal access token}'" >> ~/.config/fish/config.fish

    # zsh
    echo "export POETRY_HTTP_BASIC_{{ cookiecutter.private_package_repository_name|upper }}_USERNAME='{personal access token name}'" >> ~/.zshenv
    echo "export POETRY_HTTP_BASIC_{{ cookiecutter.private_package_repository_name|upper }}_PASSWORD='{personal access token}'" >> ~/.zshenv
    ```
{%- endif %}
{%- else -%}
1. [Generate an SSH key and add it to your authentication agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent), and [add the SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).
{%- if cookiecutter.private_package_repository_name %}
1. [Configure Poetry's credentials for this package's private repository](https://python-poetry.org/docs/repositories/#configuring-credentials):
    ```bash
    # bash
    echo "export POETRY_HTTP_BASIC_{{ cookiecutter.private_package_repository_name|upper }}_USERNAME='{username}'" >> ~/.bash_profile
    echo "export POETRY_HTTP_BASIC_{{ cookiecutter.private_package_repository_name|upper }}_PASSWORD='{password}'" >> ~/.bash_profile
    
    # fish
    echo "set --export POETRY_HTTP_BASIC_{{ cookiecutter.private_package_repository_name|upper }}_USERNAME '{username}'" >> ~/.config/fish/config.fish
    echo "set --export POETRY_HTTP_BASIC_{{ cookiecutter.private_package_repository_name|upper }}_PASSWORD '{password}'" >> ~/.config/fish/config.fish

    # zsh
    echo "export POETRY_HTTP_BASIC_{{ cookiecutter.private_package_repository_name|upper }}_USERNAME='{username}'" >> ~/.zshenv
    echo "export POETRY_HTTP_BASIC_{{ cookiecutter.private_package_repository_name|upper }}_PASSWORD='{password}'" >> ~/.zshenv
    ```
{%- endif %}
{%- endif %}
1. [Install Docker Desktop](https://www.docker.com/get-started).
1. [Configure Docker and Docker Compose to use the BuildKit build system](https://pythonspeed.com/articles/docker-buildkit/):
    ```bash
    # bash
    echo "export DOCKER_BUILDKIT=1" >> ~/.bash_profile
    echo "export COMPOSE_DOCKER_CLI_BUILD=1" >> ~/.bash_profile

    # fish
    echo "set --export DOCKER_BUILDKIT 1" >> ~/.config/fish/config.fish
    echo "set --export COMPOSE_DOCKER_CLI_BUILD 1" >> ~/.config/fish/config.fish
    
    # zsh
    echo "export DOCKER_BUILDKIT=1" >> ~/.zshenv
    echo "export COMPOSE_DOCKER_CLI_BUILD=1" >> ~/.zshenv
    ```
1. [Install VS Code](https://code.visualstudio.com/) and [VS Code's Remote-Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). Alternatively, install [PyCharm](https://www.jetbrains.com/pycharm/download/).
1. _Optional:_ [Install FiraCode Nerd Font](https://www.nerdfonts.com/font-downloads) with `brew tap homebrew/cask-fonts && brew install --cask font-fira-code-nerd-font` and [configure VS Code](https://github.com/tonsky/FiraCode/wiki/VS-Code-Instructions) or [configure PyCharm](https://github.com/tonsky/FiraCode/wiki/Intellij-products-instructions) to use `'FiraCode Nerd Font'`.

</details>

<details open>
<summary>Setup: once per project</summary>

1. Clone this repository.
2. Open the cloned repository in VS Code and run <kbd>⌘</kbd> + <kbd>⇧</kbd> + <kbd>P</kbd> > _Remote-Containers: Reopen in Container_ to start a [Development Container](https://code.visualstudio.com/docs/remote/containers). Alternatively, open the cloned repository in PyCharm and [configure Docker Compose as a remote interpreter](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html#docker-compose-remote).
3. Run `poe install` in the development environment to create the Python environment and register [pre-commit](https://pre-commit.com/). This happens automatically in VS Code, but needs to be done manually in PyCharm.

</details>

<details open>
<summary>Developing</summary>

- This project's [development environment](#development-environment) is managed by [Docker Compose](https://docs.docker.com/compose/) with `docker-compose.yml` and `Dockerfile`, while its dependencies are specified with [Poetry](https://github.com/python-poetry/poetry) in `pyproject.toml` and `poetry.lock`.
- This project follows the [Conventional Commits](https://www.conventionalcommits.org/) standard to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/) with [Commitizen](https://github.com/commitizen-tools/commitizen). Every commit is linted by [pre-commit](https://pre-commit.com/) with the linters listed in `.pre-commit-config.yaml`. All linters are configured in `pyproject.toml`.
- Run `poe` from within the development environment to print a list of [Poe the Poet](https://github.com/nat-n/poethepoet) tasks available to run on this project.
- Run `poetry add {package}` from within the development environment to install a run time dependency and add it to `poetry.lock`. Add `--group dev` if you only need the package for local development, or `--group ci` if you only need the package for linting or testing.
- Run `poetry update` from within the development environment to upgrade all dependencies to the latest versions allowed by `pyproject.toml`.

</details>
