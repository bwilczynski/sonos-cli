import click

from auth import login
from households import households


@click.group()
def cli():
    pass


cli.add_command(login)
cli.add_command(households)

if __name__ == '__main__':
    cli()
