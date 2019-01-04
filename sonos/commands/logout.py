import click

from sonos.config import creds_store


@click.command()
def logout():
    creds_store.delete_access_token()
