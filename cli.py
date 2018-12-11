import click

from commands import login, logout, get, set, play, pause, next, prev, status, volume


@click.group()
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

if __name__ == '__main__':
    cli()
