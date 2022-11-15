# {{ cookiecutter.package_name }}

{{ cookiecutter.package_description }}

## Using

To add and install this package as a dependency of your project, run `poetry add {{ cookiecutter.__package_name_kebab_case }}`.
{%- if cookiecutter.with_typer_cli|int %}

To view this app's CLI commands once it's installed, run `{{ cookiecutter.__package_name_kebab_case }} --help`.
{%- endif %}
{%- if cookiecutter.with_fastapi_api|int or cookiecutter.with_streamlit_app|int %}

To serve this app, run `docker compose up app` and open [localhost:8000](http://localhost:8000) in your browser. Within the Dev Container, this is equivalent to running {% if cookiecutter.with_fastapi_api|int %}`poe serve`{% else %}`poe streamlit`{% endif %}.
{%- endif %}

## Contributing

### Local development setup

<details>
<summary>One-time device setup</summary>

{% if cookiecutter.continuous_integration == "GitLab" -%}
1. [Generate an SSH key](https://docs.gitlab.com/ee/ssh/README.html#generate-an-ssh-key-pair) and [add the SSH key to your GitLab account](https://docs.gitlab.com/ee/ssh/README.html#add-an-ssh-key-to-your-gitlab-account).
2. Configure SSH to automatically load your SSH keys:
    ```sh
    cat << EOF >> ~/.ssh/config
    Host *
      AddKeysToAgent yes
      IgnoreUnknown UseKeychain
      UseKeychain yes
    EOF
    ```
{%- if cookiecutter.private_package_repository_name %}
1. [Create a personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token) with the `api` scope and use it to [add your private package repository credentials to your Poetry's `auth.toml` file](https://python-poetry.org/docs/repositories/#configuring-credentials):
    ```toml
    # Linux:   ~/.config/pypoetry/auth.toml
    # macOS:   ~/Library/Application Support/pypoetry/auth.toml
    # Windows: C:\Users\%USERNAME%\AppData\Roaming\pypoetry\auth.toml
    [http-basic.{{ cookiecutter.private_package_repository_name|slugify }}]
    username = "{personal access token name}"
    password = "{personal access token}"
    ```
{%- endif %}
{%- else -%}
1. [Generate an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key) and [add the SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).
1. Configure SSH to automatically load your SSH keys:
    ```sh
    cat << EOF >> ~/.ssh/config
    Host *
      AddKeysToAgent yes
      IgnoreUnknown UseKeychain
      UseKeychain yes
    EOF
    ```
{%- if cookiecutter.private_package_repository_name %}
1. [Add your private package repository credentials to your Poetry's `auth.toml` file](https://python-poetry.org/docs/repositories/#configuring-credentials):
    ```toml
    # Linux:   ~/.config/pypoetry/auth.toml
    # macOS:   ~/Library/Application Support/pypoetry/auth.toml
    # Windows: C:\Users\%USERNAME%\AppData\Roaming\pypoetry\auth.toml
    [http-basic.{{ cookiecutter.private_package_repository_name|slugify }}]
    username = "{username}"
    password = "{password}"
    ```
{%- endif %}
{%- endif %}
1. [Install Docker Desktop](https://www.docker.com/get-started).
    - Enable _Use Docker Compose V2_ in Docker Desktop's preferences window.
    - _Linux only_:
        - [Configure Docker and Docker Compose to use the BuildKit build system](https://docs.docker.com/develop/develop-images/build_enhancements/#to-enable-buildkit-builds). On macOS and Windows, BuildKit is enabled by default in Docker Desktop.
        - Export your user's user id and group id so that [files created in the Dev Container are owned by your user](https://github.com/moby/moby/issues/3206):
            ```sh
            cat << EOF >> ~/.bashrc
            export UID=$(id --user)
            export GID=$(id --group)
            {%- if cookiecutter.private_package_repository_name %}
            export POETRY_AUTH_TOML_PATH="~/.config/pypoetry/auth.toml"
            {%- endif %}
            EOF
            ```
    {%- if cookiecutter.private_package_repository_name %}
    - _Windows only_:
        - Export the location of your private package repository credentials so that Docker Compose can load these as a [build and run time secret](https://docs.docker.com/compose/compose-file/compose-file-v3/#secrets-configuration-reference):
            ```bat
            setx POETRY_AUTH_TOML_PATH %APPDATA%\pypoetry\auth.toml
            ```
    {%- endif %}
1. [Install VS Code](https://code.visualstudio.com/) and [VS Code's Remote-Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). Alternatively, install [PyCharm](https://www.jetbrains.com/pycharm/download/).
    - _Optional:_ install a [Nerd Font](https://www.nerdfonts.com/font-downloads) such as [FiraCode Nerd Font](https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts/FiraCode) with `brew tap homebrew/cask-fonts && brew install --cask font-fira-code-nerd-font` and [configure VS Code](https://github.com/tonsky/FiraCode/wiki/VS-Code-Instructions) or [configure PyCharm](https://github.com/tonsky/FiraCode/wiki/Intellij-products-instructions) to use `'FiraCode Nerd Font'`.

</details>

<details open>
<summary>One-time project setup</summary>

1. Clone this repository.
2. Start a [Dev Container](https://code.visualstudio.com/docs/remote/containers) in your preferred development environment:
    - _VS Code_: open the cloned repository and run <kbd>Ctrl/⌘</kbd> + <kbd>⇧</kbd> + <kbd>P</kbd> → _Remote-Containers: Reopen in Container_.
    - _PyCharm_: open the cloned repository and select the `dev` service when [configuring Docker Compose as a remote interpreter](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html#docker-compose-remote).
    - _Terminal_: open the cloned repository and run `docker compose up --detach dev` to start the Dev Container in the background, and then run `docker compose exec dev zsh` to open a shell prompt in the Dev Container.

</details>
{%- if cookiecutter.continuous_integration == "GitHub" %}

### Browser development setup

1. Open [{{ cookiecutter.package_url }}]({{ cookiecutter.package_url }}) in your browser.
2. Click on _Code_ and select _Create codespace_ to start a Dev Container with [GitHub Codespaces](https://github.com/features/codespaces).
{%- endif %}

### Developing
{% if cookiecutter.with_conventional_commits|int %}
- This project follows the [Conventional Commits](https://www.conventionalcommits.org/) standard to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/) with [Commitizen](https://github.com/commitizen-tools/commitizen).
{%- endif %}
- Run `poe` from within the development environment to print a list of [Poe the Poet](https://github.com/nat-n/poethepoet) tasks available to run on this project.
- Run `poetry add {package}` from within the development environment to install a run time dependency and add it to `pyproject.toml` and `poetry.lock`. Add `--group test` or `--group dev` to install a CI or development dependency, respectively.
- Run `poetry update` from within the development environment to upgrade all dependencies to the latest versions allowed by `pyproject.toml`.
{%- if cookiecutter.with_conventional_commits|int %}
- Run `cz bump` to bump the package's version, update the `CHANGELOG.md`, and create a git tag.
{%- endif %}

</details>
