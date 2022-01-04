import os
import json
import subprocess

from pathlib import Path

PROJECT_ROOT = Path(__file__).absolute().parent.parent


def _get_packages_path():
    packages_path = (
        subprocess.check_output(["pdm", "info", "--packages"]).decode("utf-8").strip()
    )
    return Path(packages_path).relative_to(PROJECT_ROOT).as_posix()


def write_vscode_settings():
    packages_path = _get_packages_path()
    if os.name == "nt":
        pytest_path = "Scripts/pytest.exe"
    else:
        pytest_path = "bin/pytest"

    data = {
        "python.analysis.extraPaths": [f"{packages_path}/lib"],
        "python.autoComplete.extraPaths": [f"{packages_path}/lib"],
    }

    settings = PROJECT_ROOT / ".vscode/settings.json"

    if Path(settings).exists():
        reply = str(
            input(
                "Detected existing Visual Studio Code settings at "
                f"{settings}. Overwrite? (y/N) "
            )
        )
        reply = reply[0].lower().strip() if reply else "n"

        if reply != "y":
            return

    settings.parent.mkdir(exist_ok=True)
    settings.write_text(json.dumps(data, indent=4))


if __name__ == "__main__":
    write_vscode_settings()
