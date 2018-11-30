import click

from auth import login


@click.group()
def cli():
    pass


cli.add_command(login)

if __name__ == '__main__':
    cli()
