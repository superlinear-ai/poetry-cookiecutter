"""Streamlit app."""

from importlib.metadata import version

import streamlit as st

st.title(f"{{ cookiecutter.package_name }} v{version('{{ cookiecutter.package_name|slugify }}')}")  # type: ignore[no-untyped-call]
