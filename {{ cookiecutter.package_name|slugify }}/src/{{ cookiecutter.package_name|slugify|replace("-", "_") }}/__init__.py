"""{{ cookiecutter.package_name }} package."""
{%- if cookiecutter.with_fastapi_api|int or cookiecutter.with_streamlit_app|int %}

import logging

import coloredlogs


def configure_root_logger() -> None:
    """Configure the root logger."""
    # Remove all handlers associated with the root logger object.
    for handler in logging.root.handlers:
        logging.root.removeHandler(handler)
    # Add coloredlogs' coloured StreamHandler to the root logger.
    coloredlogs.install()


configure_root_logger()
{%- endif %}
