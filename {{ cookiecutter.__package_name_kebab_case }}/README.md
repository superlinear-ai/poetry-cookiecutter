[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url={{ cookiecutter.package_url.replace("https://", "git@").replace(".com/", ".com:") if cookiecutter.private_package_repository_url else cookiecutter.package_url }})

# {{ cookiecutter.package_name }}

{{ cookiecutter.package_description }}

## Using

{% if cookiecutter.with_fastapi_api|int or cookiecutter.with_typer_cli|int or cookiecutter.with_streamlit_app|int %}_Python package_: t{% else %}T{% endif %}o add and install this package as a dependency of your project, run `poetry add {{ cookiecutter.__package_name_kebab_case }}`.
{%- if cookiecutter.with_typer_cli|int %}

_Python CLI_: to view this app's CLI commands once it's installed, run `{{ cookiecutter.__package_name_kebab_case }} --help`.
{%- endif %}
{%- if cookiecutter.with_fastapi_api|int or cookiecutter.with_streamlit_app|int %}

_Python application_: to serve this {% if cookiecutter.with_fastapi_api|int %}REST API{% else %}Streamlit app{% endif %}, run `docker compose up app` and open [localhost:8000](http://localhost:8000) in your browser. Within the Dev Container, this is equivalent to running {% if cookiecutter.with_fastapi_api|int %}`poe api`{% else %}`poe app`{% endif %}.
{%- endif %}

{%- if cookiecutter.with_ml_training|int or cookiecutter.with_ml_inference|int %}
## Developing
{%- if cookiecutter.with_ml_training|int %}
_Provisioning Datasets_: This package has `DVC` enabled. Here's an example of your very first dataset if you don't have one yet: 

<details>
<summary>Adding DVC Datasets</summary>

```python
"""Get the MNIST dataset."""

import boto3
from torchvision import datasets, transforms

region = boto3.Session().region_name

datasets.MNIST.mirrors = [
    f"https://sagemaker-example-files-prod-{region}.s3.amazonaws.com/datasets/image/MNIST/"
]

train_set = datasets.MNIST(
    "../data/",
    download=True,
    transform=transforms.Compose(
        [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
    ),
)
```

then you may run: 

```bash
dvc add data/
dvc push
```

This will make the Dataset available at the S3 path that has been specified at repository creation and available to Sagemaker during training. It will also create a `data.dvc` file that you can commit to your repository. 
</details>
{%- endif %}
{%- if cookiecutter.with_ml_inference|int %}
_Inference Endpoint_: Once a Sagemaker endpoint is deployed, it is important to test its functionality. Here is an example of how to test your endpoint before deploying it to an API gateway: 

<details>
<summary>Testing Sagemaker Endpoint</summary>

```python
import json

import boto3
from src.{{cookiecutter.__package_name_snake_case}}.settings import Settings

SETTINGS = Settings()
sagemaker_runtime = boto3.client('sagemaker-runtime')
# This example is for a .png file, but you can change the content type to match your payload
with open('../data/4.png', 'rb') as f:
    payload = f.read()
    try:
        response = sagemaker_runtime.invoke_endpoint(
            EndpointName=SETTINGS.github_sha[:7],
            ContentType='application/octet-stream',  # Change this depending on your payload format
            Accept='application/json',
            Body=payload
        )
    except Exception as e:
        raise(e)
json_body = json.loads(response['Body'].read().decode('utf-8'))
json_body['prediction'][0]
```
</details>

{%- endif %}
{%- endif %}
## Contributing

<details>
<summary>Prerequisites</summary>

<details>
<summary>1. Set up Git to use SSH</summary>

{% if cookiecutter.continuous_integration == "GitLab" -%}
1. [Generate an SSH key](https://docs.gitlab.com/ee/ssh/README.html#generate-an-ssh-key-pair) and [add the SSH key to your GitLab account](https://docs.gitlab.com/ee/ssh/README.html#add-an-ssh-key-to-your-gitlab-account).
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
    EOF
    ```

</details>

<details>
<summary>2. Install Docker</summary>

1. [Install Docker Desktop](https://www.docker.com/get-started).
    - Enable _Use Docker Compose V2_ in Docker Desktop's preferences window.
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
1. ⭐️ _Dev Container (with container volume)_: click on [Open in Dev Containers](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url={{ cookiecutter.package_url.replace("https://", "git@").replace(".com/", ".com:") if cookiecutter.private_package_repository_url else cookiecutter.package_url }}) to clone this repository in a container volume and create a Dev Container with VS Code.
</details>

<details>
<summary>Developing</summary>
{% if cookiecutter.with_conventional_commits|int %}
- This project follows the [Conventional Commits](https://www.conventionalcommits.org/) standard to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/) with [Commitizen](https://github.com/commitizen-tools/commitizen).
{%- endif %}
- Run `poe` from within the development environment to print a list of [Poe the Poet](https://github.com/nat-n/poethepoet) tasks available to run on this project.
- Run `poetry add {package}` from within the development environment to install a run time dependency and add it to `pyproject.toml` and `poetry.lock`. Add `--group test` or `--group dev` to install a CI or development dependency, respectively.
- Run `poetry update` from within the development environment to upgrade all dependencies to the latest versions allowed by `pyproject.toml`.
{%- if cookiecutter.with_ml_training|int %}
- Run `poe dockerize-requirements` from within the development environment to add training requirements to a Sagemaker package. 
{%- endif %}
{%- if cookiecutter.with_conventional_commits|int %}
- Run `cz bump` to bump the package's version, update the `CHANGELOG.md`, and create a git tag.
{%- endif %}

</details>
