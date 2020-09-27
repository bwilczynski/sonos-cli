import click

from sonos.api import control
from sonos.config import active_group_store
from sonos.decorators import login_required


@click.command()
@click.option("--playlist-id", "-p")
@login_required
def play(playlist_id):
    group_id = active_group_store.get_active_group()
    if playlist_id:
        control.load_playlist(group_id, playlist_id, play_on_completion=True)
    else:
        control.play(group_id)
