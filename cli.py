import click

from auth import login, logout
from households import households
from groups import groups

@click.group()
def cli():
    pass


cli.add_command(login)
cli.add_command(logout)
cli.add_command(households)
cli.add_command(groups)

if __name__ == '__main__':
    cli()
