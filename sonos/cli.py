import click

from sonos.commands import (
    login,
    logout,
    get,
    set,
    play,
    pause,
    next,
    prev,
    status,
    volume,
    set_config,
)


@click.group()
@click.version_option()
def cli():
    pass


cli.add_command(login)
cli.add_command(logout)
cli.add_command(get)
cli.add_command(set)
cli.add_command(next)
cli.add_command(pause)
cli.add_command(play)
cli.add_command(prev)
cli.add_command(status)
cli.add_command(volume)
cli.add_command(set_config)

if __name__ == "__main__":
    cli()
