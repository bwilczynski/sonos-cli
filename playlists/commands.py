import click

from api import control
from auth import login_required
from config.active_group_store import get_active_group


@click.group()
def playlists():
    pass


@playlists.command('load')
@click.option('--playlist-id', '-p', required=True)
@click.option('--autoplay', '-a', is_flag=True)
@login_required
def load_playlist(playlist_id, autoplay):
    group_id = get_active_group()
    control.load_playlist(group_id, playlist_id, autoplay)
