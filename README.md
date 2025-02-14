[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTE3IDE2VjdsLTYgNU0yIDlWOGwxLTFoMWw0IDMgOC04aDFsNCAyIDEgMXYxNGwtMSAxLTQgMmgtMWwtOC04LTQgM0gzbC0xLTF2LTFsMy0zIi8+PC9zdmc+)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/superlinear-ai/substrate) [![Open in GitHub Codespaces](https://img.shields.io/static/v1?label=GitHub%20Codespaces&message=Open&color=blue&logo=github)](https://github.com/codespaces/new/superlinear-ai/substrate) [![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-black.json)](https://github.com/copier-org/copier)

# 🌱 Substrate

A modern [Copier template](https://github.com/copier-org/copier) for scaffolding Python packages and apps.

<!-- TODO: Remove the Demo section below with a mp4 demo.

## 🍿 Demo

See 👖 [Conformal Tights](https://github.com/superlinear-ai/conformal-tights) for an example of a Python package that is scaffolded with this template. Contributing to this package can be done with a single click by [starting a GitHub Codespace](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=765698489&skip_quickstart=true) or [starting a Dev Container](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/superlinear-ai/conformal-tights).

-->

## 🎁 Features

- 🧑‍💻 One-click development environments with [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers) and [GitHub Codespaces](https://github.com/features/codespaces)
- 🌈 Cross-platform support for Linux, macOS, and Windows
- 🐚 Modern shell prompt with [Starship](https://github.com/starship/starship)
- 📦 Packaging and dependency management with [uv](https://github.com/astral-sh/uv)
- 🚚 Installing from and publishing to [PyPI](https://pypi.org/)
- ⚡️ Task running with [Poe the Poet](https://github.com/nat-n/poethepoet)
- 💅 Code formatting with [Ruff](https://github.com/charliermarsh/ruff)
- ✅ Code linting with [Pre-commit](https://pre-commit.com/), [Mypy](https://github.com/python/mypy), and [Ruff](https://github.com/charliermarsh/ruff)
- 🏷 Optionally follow the [Conventional Commits](https://www.conventionalcommits.org/) standard
- 🚦 Release new versions with [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/) using [Commitizen](https://github.com/commitizen-tools)
- 💌 Verified commits with [GPG](https://gnupg.org/)
- ♻️ Continuous integration with [GitHub Actions](https://docs.github.com/en/actions) or [GitLab CI/CD](https://docs.gitlab.com/ee/ci/)
- 🧪 Test coverage with [Coverage.py](https://github.com/nedbat/coveragepy)
- 🧰 Dependency updates with [Dependabot](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates)

## ✨ Using

> [!TIP]
> You should first [install uv](https://docs.astral.sh/uv/getting-started/installation/) to be able to run the commands below.

### Create a new Python project

To create a new Python project with this template, run:

```sh
uvx copier copy gh:superlinear-ai/substrate path/to/local/repository
```

### Update your Python project

To update your Python project to the latest template version, run:

```sh
uvx copier update
```

### Release a new version of your Python project

If you have enabled [Conventional Commits](https://www.conventionalcommits.org/), you can create a new version tag and update `CHANGELOG.md` based on your commit messages with:

```sh
git checkout main
cz bump
git push origin main --tags
```

## 🍪 Migrating from Cookiecutter

> [!IMPORTANT]
> This project was formerly known as `Poetry Cookiecutter` and was based on [Poetry](https://github.com/python-poetry/poetry) and [Cookiecutter](https://github.com/cookiecutter/cookiecutter). We will continue to support the original Cookiecutter-based template side by side with the new Copier-based template. However, we do encourage users to upgrade to the new Copier-based template by following the instructions below.

To migrate a project from Cookiecutter to Copier, follow these steps:

1. In your project repository, run:

    ```sh
    # Create a new branch
    git checkout -b rescaffold

    # Remove files specific to Poetry
    rm -f poetry.lock
    
    # Rescaffold the project without changing src/ and tests/
    uvx copier copy --overwrite --exclude src/ --exclude tests/ gh:superlinear-ai/substrate .
    ```

2. Review the changes to `pyproject.toml` and reinsert your project's dependencies.
3. Review the changes to `README.md` and reinsert your project's documentation.
4. Commit and push all changes with:

    ```sh
    # Stage all changes
    git add .

    # Commit the staged changes
    git commit -m "build: upgrade scaffolding"

    # Push the committed changes
    git push origin rescaffold
    ```

5. Create a PR from your branch, review it, and merge it!
