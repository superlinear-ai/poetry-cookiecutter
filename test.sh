#!/bin/bash

set -e

rm -rf my-project

project_types=("app" "package")
typing_options=("optional" "strict")

for project_type in "${project_types[@]}"; do
    for typing in "${typing_options[@]}"; do
        # Scaffold a Python project
        uvx copier copy --vcs-ref=HEAD . my-project \
            --defaults \
            --data project_type="$project_type" \
            --data project_name="My Project" \
            --data project_description="A Python $project_type that reticulates splines." \
            --data project_url="https://github.com/user/repo" \
            --data author_name="John Smith" \
            --data author_email="john@example.com" \
            --data python_version="3.10" \
            --data typing="$typing" \
            --data with_fastapi_api=true \
            --data with_typer_cli="$([ "$project_type" == "app" ] && echo false || echo true)"

        cd my-project
        git config --global init.defaultBranch main
        git init
        git checkout -b test
        git add .

        # Lint and test the project with a dev container
        devcontainer up --remove-existing-container --workspace-folder .
        devcontainer exec --workspace-folder . uv lock
        devcontainer exec --workspace-folder . poe lint
        devcontainer exec --workspace-folder . poe test

        # Build and test the app service if project type is 'app'
        if [ "$project_type" == "app" ]; then
            docker compose build app
            docker compose up --detach app
            sleep 2
            if ! curl -f 'http://localhost:8000/compute?n=8' > /dev/null; then
                docker compose down
                exit 1
            fi
        fi

        cd -
        rm -rf my-project
    done
done
