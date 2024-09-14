[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url={{ cookiecutter.project_url.replace("https://", "git@").replace(".com/", ".com:") if cookiecutter.private_package_repository_url else cookiecutter.project_url }}){% if cookiecutter.continuous_integration == "GitHub" %} [![Open in GitHub Codespaces](https://img.shields.io/static/v1?label=GitHub%20Codespaces&message=Open&color=blue&logo=github)](https://github.com/codespaces/new/{{ cookiecutter.project_url.replace("https://github.com/", "") }}){% endif %}

# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}
{%- if cookiecutter.project_type == "package" or cookiecutter.with_typer_cli|int %}

## Installing

To install this package, run:

```sh
{% if cookiecutter.private_package_repository_name %}poetry add{% else %}pip install{% endif %} {{ cookiecutter.__project_name_kebab_case }}
```
{%- endif %}

## Using
{%- if cookiecutter.with_typer_cli|int %}

To view the CLI help information, run:

```sh
{{ cookiecutter.__project_name_kebab_case }} --help
```
{%- elif cookiecutter.project_type == "app" %}

To serve this app, run:

```sh
docker compose up app
```
{%- if cookiecutter.with_fastapi_api|int %}

and open [localhost:8000](http://localhost:8000) in your browser.
{%- endif %}

Within the Dev Container this is equivalent to:

```sh
poe {% if cookiecutter.with_fastapi_api|int %}api{% else %}app{% endif %}
```
{%- else %}

Example usage:

```python
import {{ cookiecutter.__project_name_snake_case }}

...
```
{%- endif %}

## Contributing

<details>
<summary>Prerequisites</summary>

<details>
<summary>1. Set up Git to use SSH</summary>

{% if cookiecutter.continuous_integration == "GitLab" -%}
1. [Generate an SSH key](https://docs.gitlab.com/ee/user/ssh.html#generate-an-ssh-key-pair) and [add the SSH key to your GitLab account](https://docs.gitlab.com/ee/user/ssh.html#add-an-ssh-key-to-your-gitlab-account).
{%- else -%}
1. [Generate an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key) and [add the SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).
{%- endif %}
1. Configure SSH to automatically load your SSH keys:
    ```sh
    cat << EOF >> ~/.ssh/config
    
    Host *
      AddKeysToAgent yes
      IgnoreUnknown UseKeychain
      UseKeychain yes
      ForwardAgent yes
    EOF
    ```

</details>

<details>
<summary>2. Install Docker</summary>

1. [Install Docker Desktop](https://www.docker.com/get-started).
    - _Linux only_:
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

</details>

<details>
<summary>3. Install VS Code or PyCharm</summary>

1. [Install VS Code](https://code.visualstudio.com/) and [VS Code's Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). Alternatively, install [PyCharm](https://www.jetbrains.com/pycharm/download/).
2. _Optional:_ install a [Nerd Font](https://www.nerdfonts.com/font-downloads) such as [FiraCode Nerd Font](https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts/FiraCode) and [configure VS Code](https://github.com/tonsky/FiraCode/wiki/VS-Code-Instructions) or [configure PyCharm](https://github.com/tonsky/FiraCode/wiki/Intellij-products-instructions) to use it.

</details>
{%- if cookiecutter.private_package_repository_name %}

<details>
<summary>4. Configure Poetry to use the private package repository</summary>

{% if cookiecutter.continuous_integration == "GitLab" -%}
1. [Create a personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token) with the `api` scope and use it to [add your private package repository credentials to your Poetry's `auth.toml` file](https://python-poetry.org/docs/repositories/#configuring-credentials):
    ```toml
    # Linux:   ~/.config/pypoetry/auth.toml
    # macOS:   ~/Library/Application Support/pypoetry/auth.toml
    # Windows: C:\Users\%USERNAME%\AppData\Roaming\pypoetry\auth.toml
    [http-basic.{{ cookiecutter.private_package_repository_name|slugify }}]
    username = "{personal access token name}"
    password = "{personal access token}"
    ```
{%- else -%}
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

</details>
{%- endif %}

</details>

<details open>
<summary>Development environments</summary>

The following development environments are supported:
{% if cookiecutter.continuous_integration == "GitHub" %}
1. ⭐️ _GitHub Codespaces_: click on _Code_ and select _Create codespace_ to start a Dev Container with [GitHub Codespaces](https://github.com/features/codespaces).
{%- endif %}
1. ⭐️ _Dev Container (with container volume)_: click on [Open in Dev Containers](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url={{ cookiecutter.project_url.replace("https://", "git@").replace(".com/", ".com:") if cookiecutter.private_package_repository_url else cookiecutter.project_url }}) to clone this repository in a container volume and create a Dev Container with VS Code.
1. _Dev Container_: clone this repository, open it with VS Code, and run <kbd>Ctrl/⌘</kbd> + <kbd>⇧</kbd> + <kbd>P</kbd> → _Dev Containers: Reopen in Container_.
1. _PyCharm_: clone this repository, open it with PyCharm, and [configure Docker Compose as a remote interpreter](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html#docker-compose-remote) with the `dev` service.
1. _Terminal_: clone this repository, open it with your terminal, and run `docker compose up --detach dev` to start a Dev Container in the background, and then run `docker compose exec dev zsh` to open a shell prompt in the Dev Container.

</details>

<details>
<summary>Developing</summary>
{% if cookiecutter.with_conventional_commits|int %}
- This project follows the [Conventional Commits](https://www.conventionalcommits.org/) standard to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/) with [Commitizen](https://github.com/commitizen-tools/commitizen).
{%- endif %}
- Run `poe` from within the development environment to print a list of [Poe the Poet](https://github.com/nat-n/poethepoet) tasks available to run on this project.
- Run `poetry add {package}` from within the development environment to install a run time dependency and add it to `pyproject.toml` and `poetry.lock`. Add `--group test` or `--group dev` to install a CI or development dependency, respectively.
- Run `poetry update` from within the development environment to upgrade all dependencies to the latest versions allowed by `pyproject.toml`.
{%- if cookiecutter.with_conventional_commits|int %}
- Run `cz bump` to bump the {{ cookiecutter.project_type }}'s version, update the `CHANGELOG.md`, and create a git tag.
{%- endif %}

</details>
