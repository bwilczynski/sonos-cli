import click

from api import control
from auth import login_required
from decorators import format_result, output_option
from groups import get_active_group
from households import get_active_household

household_id = get_active_household()


@click.group()
def playlists():
    pass


@playlists.command('list')
@output_option()
@login_required
@format_result(headers=['id', 'name'])
def list_playlists():
    result = control.get_playlists(household_id)
    return result['playlists']


@playlists.command()
@click.option('--playlist-id', '-p', required=True)
@output_option()
@login_required
@format_result(headers=['name', 'album', 'artist'])
def list_tracks(playlist_id):
    result = control.get_tracks(household_id, playlist_id)
    return result['tracks']


@playlists.command('load')
@click.option('--playlist-id', '-p', required=True)
@click.option('--autoplay', '-a', is_flag=True)
@login_required
def load_playlist(playlist_id, autoplay):
    group_id = get_active_group()
    control.load_playlist(group_id, playlist_id, autoplay)
