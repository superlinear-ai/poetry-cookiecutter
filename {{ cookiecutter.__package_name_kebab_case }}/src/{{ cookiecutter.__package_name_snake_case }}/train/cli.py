"""{{ cookiecutter.package_name }} CLI."""

import typer

app = typer.Typer()


@app.command()
def express(message: str = "") -> None:
    """Say a message."""
    typer.echo(message)
