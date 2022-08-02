"""Streamlit app."""

from importlib.metadata import version

import streamlit as st

st.title(f"{{ cookiecutter.package_name }} v{version('{{ cookiecutter.__package_name_kebab_case }}')}")  # type: ignore[no-untyped-call]
