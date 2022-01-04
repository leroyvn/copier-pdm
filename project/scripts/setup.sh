#!/usr/bin/env bash
set -e

install_with_pipx() {
    if ! command -v "$1" &>/dev/null; then
        if ! command -v pipx &>/dev/null; then
            python3 -m pip install --user pipx
        fi
        pipx install "$1"
    fi
}

install_with_pipx pdm
install_with_pipx nox
pdm install
