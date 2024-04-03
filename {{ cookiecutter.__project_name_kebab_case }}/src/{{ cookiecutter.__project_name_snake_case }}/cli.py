"""{{ cookiecutter.project_name }} CLI."""

import typer
from rich import print

app = typer.Typer()


@app.command()
def fire(name: str = "Chell") -> None:
    """Fire portal gun."""
    print(f"[bold red]Alert![/bold red] {name} fired [green]portal gun[/green] :boom:")
