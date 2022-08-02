"""{{ cookiecutter.package_name }} CLI."""

import typer

app = typer.Typer()


@app.command()
def say(message: str = "") -> None:
    """Say a message."""
    typer.echo(message)
