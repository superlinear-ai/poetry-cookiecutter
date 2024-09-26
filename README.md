[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/radix-ai/poetry-cookiecutter) [![Open in GitHub Codespaces](https://img.shields.io/static/v1?label=GitHub%20Codespaces&message=Open&color=blue&logo=github)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=444870763)

# Baseline app Cookiecutter

A modern [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for scaffolding Python packages and apps.


## 🎁 Features

- 🧑‍💻 Quick and reproducible development environments with VS Code's [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers), PyCharm's [Docker Compose interpreter](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html#docker-compose-remote), and [GitHub Codespaces](https://github.com/features/codespaces)
- 🌈 Cross-platform support for Linux, macOS (Apple silicon and Intel), and Windows
- 🐚 Modern shell prompt with [Starship](https://github.com/starship/starship)
- 📦 Packaging and dependency management with [Poetry](https://github.com/python-poetry/poetry)
- ⚡️ Task running with [Poe the Poet](https://github.com/nat-n/poethepoet)
- ✍️ Code formatting with [Ruff](https://github.com/charliermarsh/ruff)
- ✅ Code linting with [Pre-commit](https://pre-commit.com/), [Mypy](https://github.com/python/mypy), and [Ruff](https://github.com/charliermarsh/ruff)
- 🏷 Optionally follows the [Conventional Commits](https://www.conventionalcommits.org/) standard to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/) with [Commitizen](https://github.com/commitizen-tools/commitizen)
- 💌 Verified commits with [GPG](https://gnupg.org/)
- ♻️ Continuous integration with [GitHub Actions](https://docs.github.com/en/actions)
- 🧪 Test coverage with [Coverage.py](https://github.com/nedbat/coveragepy)
- 🏗 Scaffolding updates with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and [Cruft](https://github.com/cruft/cruft)
- 🧰 Dependency updates with [Dependabot](https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/about-dependabot-version-updates)
- 🤹 Task management made easy with references to PR and Issues with [Teamwork](https://baseline6.teamwork.com/app/home/activity?from=homepage)

## ✨ Using

### Creating a new Python project

To create a new Python project with this template:

1. Install the latest [Cruft](https://github.com/cruft/cruft) and [Cookiecutter](https://github.com/cookiecutter/cookiecutter) in your [Python environment](https://github.com/pyenv/pyenv-virtualenv) with:

   ```sh
   pip install --upgrade "cruft>=2.12.0" "cookiecutter>=2.1.1"
   ```


2. [Create a new repository](https://github.com/new) for your Python project, then clone it locally.
3. Run the following command in the parent directory of the cloned repository to apply the Poetry Cookiecutter template:

   ```sh
   cruft create -f https://github.com/Baseline-quebec/baseline-app-cookiecutter
   ```

   <details>

   <summary>⚠️ If your repository name ≠ the project's slugified name</summary>

   If your repository name differs from your project's slugified name (see `project_name` in the [Template parameters](https://github.com/radix-ai/poetry-cookiecutter#-template-parameters) below), you will need to copy the scaffolded project into the repository with:

      ```sh
      cp -r {project-name}/ {repository-name}/
      ```

   </details>

4. Add the remote origin to your local package.
5. _Optional:_ Link your repository to a Teamwork Project by adding the required Secrets to the Github Repository for the Teamwork Integration Github Workflow using this documentation: https://github.com/Teamwork/github-sync

### Updating your Python project

To update your Python project to the latest template version:

1. Update the project while verifying the existing template parameters and setting any new parameters, if there are any:

   ```sh
   cruft update --cookiecutter-input
   ```

2. If any of the file updates failed, resolve them by inspecting the corresponding `.rej` files.

## 🤓 Template parameters


| Parameter                                                                 | Description                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |                                                                                                      
| `project_name` <br> "Spline Reticulator"                                  | The name of the project. Will be slugified to `snake_case` for importing and `kebab-case` for installing. For example, `My Package` will be `my_package` for importing and `my-package` for installing.                                                                                                                             |
| `project_description` <br> "A Python package that reticulates splines."   | A single-line description of the project.                                                                                                                                                                                                                                                                                           |
| `project_url` <br> "<https://github.com/user/spline-reticulator>"         | The URL to the project's repository.                                                                                                                                                                                                                                                                                                |
| `author_name` <br> "John Smith"                                           | The full name of the primary author of the project.                                                                                                                                                                                                                                                                                 |
| `author_email` <br> "<john@example.com>"                                  | The email address of the primary author of the project.                                                                                                                                                                                                                                                                             |
| `python_version` <br> "3.12"                                              | The minimum Python version that the project requires.                                                                                                                                                                                                                                                                               |
| `development_environment` <br> ["simple", "strict"]                       | Whether to configure the development environment with a focus on simplicity or with a focus on strictness. In strict mode, additional [Ruff rules](https://docs.astral.sh/ruff/rules/) are added, and tools such as [Mypy](https://github.com/python/mypy) and [Pytest](https://github.com/pytest-dev/pytest) are set to strict mode. |
| `with_fastapi_api` <br> ["0", "1"]                                        | If "1", [FastAPI](https://github.com/tiangolo/fastapi) is added as a run time dependency, FastAPI API stubs and tests are added, a `poe api` command for serving the API is added.                                                                                                                                                  |
| `with_typer_cli` <br> ["0", "1"]                                          | If "1", [Typer](https://github.com/tiangolo/typer) is added as a run time dependency, Typer CLI stubs and tests are added, the package itself is registered as a CLI.                                                                                                                                                               |                                                                                            
