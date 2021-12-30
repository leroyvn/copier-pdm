import os

import nox

os.environ["PDM_IGNORE_SAVED_PYTHON"] = "1"


@nox.session(python=("3.7", "3.8", "3.9", "3.10"))
def test(session):
    session.run("pdm", "install", "-G", "tests", "-G", "duty", external=True)
    session.run("duty", "test/")
