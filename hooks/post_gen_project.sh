#!/usr/bin/env bash
set -e

# Remove .github/ if GitHub is not the selected continuous integration provider.
if [ "{{ cookiecutter.continuous_integration }}" != "GitHub" ]
then
    rm -rf .github/
fi
