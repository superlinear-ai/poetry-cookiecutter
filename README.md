# Cookiecutter Python package

A modern [cookiecutter](https://cookiecutter.readthedocs.io) template for scaffolding Python packages.

## Usage

<details open>
<summary>Setting up a new project with this cookiecutter template</summary>

1. Install [cruft](https://cruft.github.io/cruft/) in your Python environment with:
   ```bash
   pip install cruft
   ```
2. Create a new repository and give it a name in title case, e.g. "My Package".
3. Clone your newly created repository.
4. In the parent directory of the repository, run `cruft create -f git+ssh://git@github.com:radix-ai/poetry-cookiecutter.git`.

</details>

<details open>
<summary>Updating a cookiecutter project with the latest template</summary>

1. Run `cruft check` to check for updates.
2. Run `cruft update` to update to the latest scaffolding.
3. Address failed merges in any `.rej` files.

</details>
