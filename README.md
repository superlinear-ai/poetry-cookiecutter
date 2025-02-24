[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTE3IDE2VjdsLTYgNU0yIDlWOGwxLTFoMWw0IDMgOC04aDFsNCAyIDEgMXYxNGwtMSAxLTQgMmgtMWwtOC04LTQgM0gzbC0xLTF2LTFsMy0zIi8+PC9zdmc+)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/vanolucas/substrate) [![Open in GitHub Codespaces](https://img.shields.io/static/v1?label=GitHub%20Codespaces&message=Open&color=blue&logo=github)](https://github.com/codespaces/new/vanolucas/substrate) [![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-black.json)](https://github.com/copier-org/copier)

# 🌱 Substrate

A modern [Copier template](https://github.com/copier-org/copier) for scaffolding Python packages and apps.

<video src="https://github.com/user-attachments/assets/28d23137-ebae-47d8-a6e5-11f66abf2a91" controls preload></video>

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
uvx copier copy gh:vanolucas/substrate path/to/local/repository
```

### Update your Python project

To update your Python project to the latest template version, run:

```sh
uvx copier update --exclude src/ --exclude tests/
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

    # Remove unnecessary files
    rm -f .cruft.json poetry.lock
    
    # Rescaffold the project without changing src/ and tests/
    uvx copier copy --overwrite --exclude src/ --exclude tests/ gh:vanolucas/substrate .
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

## Contributing

<details>
<summary>Prerequisites</summary>

1. [Generate an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key) and [add the SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).
2. Configure SSH to automatically load your SSH keys:

    ```sh
    cat << EOF >> ~/.ssh/config
    
    Host *
      AddKeysToAgent yes
      IgnoreUnknown UseKeychain
      UseKeychain yes
      ForwardAgent yes
    EOF
    ```

3. [Install Docker Desktop](https://www.docker.com/get-started).
4. [Install VS Code](https://code.visualstudio.com/) and [VS Code's Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). Alternatively, install [PyCharm](https://www.jetbrains.com/pycharm/download/).
5. _Optional:_ install a [Nerd Font](https://www.nerdfonts.com/font-downloads) such as [FiraCode Nerd Font](https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts/FiraCode) and [configure VS Code](https://github.com/tonsky/FiraCode/wiki/VS-Code-Instructions) or [PyCharm](https://github.com/tonsky/FiraCode/wiki/Intellij-products-instructions) to use it.

</details>

<details open>
<summary>Development environments</summary>

The following development environments are supported:

1. ⭐️ _GitHub Codespaces_: click on [Open in GitHub Codespaces](https://github.com/codespaces/new/vanolucas/substrate) to start developing in your browser.
2. ⭐️ _VS Code Dev Container (with container volume)_: click on [Open in Dev Containers](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/vanolucas/substrate) to clone this repository in a container volume and create a Dev Container with VS Code.
3. ⭐️ _uv_: clone this repository and run the following from root of the repository:

    ```sh
    # Create and install a virtual environment
    uv sync

    # Activate the virtual environment
    source .venv/bin/activate

    # Install the pre-commit hooks
    pre-commit install --install-hooks
    ```

3. _VS Code Dev Container_: clone this repository, open it with VS Code, and run <kbd>Ctrl/⌘</kbd> + <kbd>⇧</kbd> + <kbd>P</kbd> → _Dev Containers: Reopen in Container_.
4. _PyCharm Dev Container_: clone this repository, open it with PyCharm, [create a Dev Container with Mount Sources](https://www.jetbrains.com/help/pycharm/start-dev-container-inside-ide.html), and [configure an existing Python interpreter](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#widget) at `/opt/venv/bin/python`.

</details>

<details open>
<summary>Developing</summary>

- This project follows the [Conventional Commits](https://www.conventionalcommits.org/) standard to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/) with [Commitizen](https://github.com/commitizen-tools/commitizen).
- Run `cz bump` to bump Substrate's version, update the `CHANGELOG.md`, and create a git tag. Then push the changes and the git tag with `git push origin main --tags`.

</details>
