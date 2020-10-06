import nox

nox.options.sessions = ["lint"]

locations = "sonos", "noxfile.py"

PYTHON_INTERPRETERS = ["3.7", "3.8"]


@nox.session(python=PYTHON_INTERPRETERS)
def lint(session):
    args = session.posargs or locations
    session.install("flake8", "flake8-black")
    session.run("flake8", *args)


@nox.session(python=PYTHON_INTERPRETERS)
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)
