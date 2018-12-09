import click

from auth import login, logout
from groups import groups
from households import households
from playback import playback
from playlists import playlists


@click.group()
def cli():
    pass


cli.add_command(login)
cli.add_command(logout)
cli.add_command(households)
cli.add_command(groups)
cli.add_command(playback)
cli.add_command(playlists)

if __name__ == '__main__':
    cli()
