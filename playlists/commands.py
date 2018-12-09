import click

from api import control
from auth import login_required
from decorators import format_result, output_option
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
