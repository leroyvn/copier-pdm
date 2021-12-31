import nox


def _no_venv(session):
    return isinstance(session.virtualenv, nox.virtualenv.PassthroughEnv)


def _has_venv(session):
    return not _no_venv(session)


def _pdm(session):
    if _no_venv(session):
        return ["pdm"]
    else:
        return ["pdm", "--ignore-python"]


@nox.session(python=("3.7", "3.8", "3.9", "3.10"))
def test(session):
    """Run the test suite."""
    pdm = _pdm(session)

    # Install only if a virtual environment is used
    # If --no-venv is used, the install step is skipped
    if _has_venv(session):
        session.run(*pdm, "install", "-G", "tests", external=True)

    # Allow passing arguments to pytest
    # Example: nox --no-venv -s tests -- tests/my_test.py
    args = session.posargs if session.posargs else ["tests"]
    session.run(*pdm, "run", "pytest", "-c", "config/pytest.ini", *args, external=True)
