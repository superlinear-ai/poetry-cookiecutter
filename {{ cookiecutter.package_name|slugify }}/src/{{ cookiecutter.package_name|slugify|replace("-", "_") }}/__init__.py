"""{{ cookiecutter.package_name }} package."""

import logging

import coloredlogs


def configure_root_logger() -> None:
    """Configure the root logger."""
    # Remove all handlers associated with the root logger object.
    for handler in logging.root.handlers:
        logging.root.removeHandler(handler)
    # Add coloredlogs' coloured StreamHandler to the root logger.
    coloredlogs.install(
        fmt="%(asctime)s %(name)s %(funcName)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
        field_styles={
            "asctime": {"color": "green"},
            "name": {"color": "blue"},
            "funcName": {"color": "magenta"},
            "levelname": {"color": "black", "bold": True},
        },
        isatty=True,
    )


configure_root_logger()
