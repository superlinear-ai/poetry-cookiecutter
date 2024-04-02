[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/radix-ai/poetry-cookiecutter) [![Open in GitHub Codespaces](https://img.shields.io/static/v1?label=GitHub%20Codespaces&message=Open&color=blue&logo=github)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=444870763)

# Poetry Cookiecutter

A modern [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for scaffolding Python packages and apps.

## 🍿 Demo

See [My Package](https://github.com/radix-ai/my-package) for an example of a Python package and app that is scaffolded with this template.

Starting development in My Package can be done with a single click by [opening My Package in GitHub Codespaces](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=450509735), or [opening My Package in a Dev Container](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/radix-ai/my-package).

## 🎁 Features

- 🧑‍💻 Quick and reproducible development environments with VS Code's [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers), PyCharm's [Docker Compose interpreter](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html#docker-compose-remote), and [GitHub Codespaces](https://github.com/features/codespaces)
- 🌈 Cross-platform support for Linux, macOS (Apple silicon and Intel), and Windows
- 🐚 Modern shell prompt with [Starship](https://github.com/starship/starship)
- 📦 Packaging and dependency management with [Poetry](https://github.com/python-poetry/poetry)
- 🚚 Installing from and publishing to private package repositories and [PyPI](https://pypi.org/)
- ⚡️ Task running with [Poe the Poet](https://github.com/nat-n/poethepoet)
- ✍️ Code formatting with [Ruff](https://github.com/charliermarsh/ruff)
- ✅ Code linting with [Pre-commit](https://pre-commit.com/), [Mypy](https://github.com/python/mypy), and [Ruff](https://github.com/charliermarsh/ruff)
- 🏷 Optionally follows the [Conventional Commits](https://www.conventionalcommits.org/) standard to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/) with [Commitizen](https://github.com/commitizen-tools/commitizen)
- 💌 Verified commits with [GPG](https://gnupg.org/)
- ♻️ Continuous integration with [GitHub Actions](https://docs.github.com/en/actions) or [GitLab CI/CD](https://docs.gitlab.com/ee/ci/)
- 🧪 Test coverage with [Coverage.py](https://github.com/nedbat/coveragepy)
- 🏗 Scaffolding updates with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and [Cruft](https://github.com/cruft/cruft)
- 🧰 Dependency updates with [Dependabot](https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/about-dependabot-version-updates)

## ✨ Using

### Creating a new Python project

To create a new Python project with this template:

1. Install the latest [Cruft](https://github.com/cruft/cruft) and [Cookiecutter](https://github.com/cookiecutter/cookiecutter) in your [Python environment](https://github.com/pyenv/pyenv-virtualenv) with:
   ```sh
   pip install --upgrade "cruft>=2.12.0" "cookiecutter>=2.1.1"
   ```
2. Create a new repository for your Python project, then clone it locally.
3. Run the following command in the parent directory of the cloned repository to apply the Poetry Cookiecutter template:
   ```sh
   cruft create -f https://github.com/radix-ai/poetry-cookiecutter
   ```
4. _Optional:_ if your repository name differs from your project's slugified package name (see `package_name` in the [Template parameters](https://github.com/radix-ai/poetry-cookiecutter#-template-parameters) below), you will need to copy the scaffolded project into the repository with:
   ```sh
   cp -r {package-name}/ {repository-name}/
   ```

### Updating your Python project

To update your Python project with the latest template:

1. Run `cruft update` to update your project with the latest template.
2. If any of the updates failed, resolve them by inspecting the generated `.rej` files.

## 🤓 Template parameters

| Parameter                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `package_name` <br> "Spline Reticulator"                                | The name of the package. Will be slugified to `snake_case` for importing and `kebab-case` for installing. For example, `My Package` will be `my_package` for importing and `my-package` for installing.                                                                                                                                                                                                                                      |
| `package_description` <br> "A Python package that reticulates splines." | A single-line description of the package.                                                                                                                                                                                                                                                                                                                                                         |
| `package_url` <br> "https://github.com/user/spline-reticulator"         | The URL to the package's repository.                                                                                                                                                                                                                                                                                                                                                              |
| `author_name` <br> "John Smith"                                         | The full name of the primary author of the package.                                                                                                                                                                                                                                                                                                                                               |
| `author_email` <br> "john@example.com"                                  | The email address of the primary author of the package.                                                                                                                                                                                                                                                                                                                                           |
| `python_version` <br> "3.8"                                             | The minimum Python version that the package requires.                                                                                                                                                                                                                                                                                                                                             |
| `docker_image` <br> "python:$PYTHON_VERSION-slim"                       | The base Docker image to use for the Dev Container and application. The $PYTHON_VERSION build argument is equal to the `python_version` value by default, but may be overridden when building the image to test different Python versions. If CUDA support is required, you may use [radixai/python-gpu:$PYTHON_VERSION-cuda11.8](https://github.com/radix-ai/python-gpu).
| `with_zscaler_cert` <br> ["0", "1"]                                             | Include the ZScaler CA Root Certificate in the devcontainer.                                                                                                                                                                                                                                                                                                                                             |                       |
| `development_environment` <br> ["simple", "strict"]                     | Whether to configure the development environment with a focus on simplicity or with a focus on strictness. In strict mode, additional [Ruff rules](https://beta.ruff.rs/docs/rules/) are added, and tools such as [Mypy](https://github.com/python/mypy) and [Pytest](https://github.com/pytest-dev/pytest) are set to strict mode.                                                               |
| `with_conventional_commits` <br> ["0", "1"]                             | If "1", [Commitizen](https://github.com/commitizen-tools/commitizen) will verify that your commits follow the [Conventional Commits](https://www.conventionalcommits.org/) standard. In return, `cz bump` may be used to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/).                                                                 |
| `with_fastapi_api` <br> ["0", "1"]                                      | If "1", [FastAPI](https://github.com/tiangolo/fastapi) is added as a run time dependency, FastAPI API stubs and tests are added, a `poe api` command for serving the API is added, and an `app` stage that packages the API is added to the Dockerfile. Additionally, the CI workflow will push the application as a Docker image instead of publishing the Python package.                       |
| `with_pydantic_typing` <br> ["0", "1"]                                  | If "1", [Pydantic](https://github.com/samuelcolvin/pydantic) is added as a run time dependency, and the [Pydantic mypy plugin](https://pydantic-docs.helpmanual.io/mypy_plugin/) is enabled and configured.                                                                                                                                                                                       |
| `with_sentry_logging` <br> ["0", "1"]                                   | If "1", [Sentry](https://github.com/getsentry/sentry-python) is added as a run time dependency, and a Sentry configuration stub and tests are added.                                                                                                                                                                                                                                              |
| `with_streamlit_app` <br> ["0", "1"]                                    | If "1", [Streamlit](https://github.com/streamlit/streamlit) is added as a run time dependency, a Streamlit application stub is added, a `poe app` command to serve the Streamlit app is added, and an `app` stage that packages the Streamlit app is added to the Dockerfile. Additionally, the CI workflow will push the application as a Docker image instead of publishing the Python package. |
| `with_typer_cli` <br> ["0", "1"]                                        | If "1", [Typer](https://github.com/tiangolo/typer) is added as a run time dependency, Typer CLI stubs and tests are added, the package itself is registered as a CLI, and an `app` stage is added to the Dockerfile that packages the CLI.                                                                                                                                                        |
| `continuous_integration` <br> ["GitHub", "GitLab"]                      | Whether to include a [GitHub Actions](https://docs.github.com/en/actions) or a [GitLab CI/CD](https://docs.gitlab.com/ee/ci/) continuous integration workflow for testing and publishing the package or app.                                                                                                                                                                                      |
| `docstring_style` <br> ["NumPy", "Google"]                              | Whether to use and validate [NumPy-style](https://numpydoc.readthedocs.io/en/latest/format.html) or [Google-style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings).                                                                                                                                                                                       |
| `private_package_repository_name` <br> "Private Package Repository"     | Optional name of a private package repository to install packages from and publish this package to.                                                                                                                                                                                                                                                                                               |
| `private_package_repository_url` <br> "https://pypi.example.com/simple" | Optional URL of a private package repository to install packages from and publish this package to. Make sure to include the `/simple` suffix. For instance, when using a GitLab Package Registry this value should be of the form `https://gitlab.com/api/v4/projects/` `{project_id}` `/packages/pypi/simple`.                                                                                   |
