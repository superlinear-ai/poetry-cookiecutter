@echo off

rem This script runs on the host before the Dev Container is created to support both bind mount and
rem volume mount workspaces [1]. If a volume mount workspace is detected, a .env file is generated
rem that tells docker-compose.yml to use the container volume as the workspace source.
rem
rem [1] https://github.com/microsoft/vscode-remote-release/issues/6561

setlocal

set CONTAINER_ID=%COMPUTERNAME%
set WORKSPACE_MOUNT_SOURCE_FMT={% raw %}{{- $source := "" }}{{- range .HostConfig.Mounts }}{{- if (and (eq .Type `"volume"`) (eq .Target `"/workspaces"`)) }}{{- $source = .Source }}{{- end }}{{- end }}{{- $source }}{% endraw %}
set WORKSPACE_CONTAINER_VOLUME_SOURCE=`docker container inspect "%CONTAINER_ID%" --format="%WORKSPACE_MOUNT_SOURCE_FMT%" 2>nul`

if "%WORKSPACE_CONTAINER_VOLUME_SOURCE%"=="" exit /b

(
echo WORKSPACE_SOURCE=devcontainer-volume
echo WORKSPACE_TARGET=/app/
echo WORKSPACE_CONTAINER_VOLUME_SOURCE=%WORKSPACE_CONTAINER_VOLUME_SOURCE%
echo WORKSPACE_IS_CONTAINER_VOLUME=true
) > .devcontainer\.env
type .devcontainer\.env

endlocal
