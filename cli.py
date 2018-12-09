import click

from auth import login, logout
from commands import get, set, play, pause, next, prev, status
from playlists import playlists


@click.group()
def cli():
    pass


cli.add_command(login)
cli.add_command(logout)
cli.add_command(playlists)

cli.add_command(get)
cli.add_command(set)
cli.add_command(next)
cli.add_command(pause)
cli.add_command(play)
cli.add_command(prev)
cli.add_command(status)

if __name__ == '__main__':
    cli()
