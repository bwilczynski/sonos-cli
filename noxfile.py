import nox

nox.options.sessions = ["lint"]

locations = "sonos", "noxfile.py"

DEFAULT_PYTHON = "3.8"


@nox.session(python=DEFAULT_PYTHON)
def lint(session):
    args = session.posargs or locations
    session.install("flake8", "flake8-black")
    session.run("flake8", *args)


@nox.session(python=DEFAULT_PYTHON)
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)
