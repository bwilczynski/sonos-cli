import click

from api import control
from config.active_group_store import get_active_group
from decorators import login_required


@click.command()
@click.option('--playlist-id', '-p')
@login_required
def play(playlist_id):
    group_id = get_active_group()
    if playlist_id:
        control.load_playlist(group_id, playlist_id, play_on_completion=True)
    else:
        control.play(group_id)
