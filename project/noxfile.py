import os

import nox

os.environ["PDM_IGNORE_SAVED_PYTHON"] = "1"


@nox.session(venv_backend="conda", python=("3.7",))
def test(session):
    session.run("pdm", "install", "-G", "tests", external=True)
    session.run("pytest", "tests/")
