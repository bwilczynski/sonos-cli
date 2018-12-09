import click

from api import control
from auth import login_required
from decorators import format_result
from households import get_active_household

household_id = get_active_household()


@click.group()
def playlists():
    pass


@playlists.command('list')
@click.option('--output', '-o', default='table')
@login_required
@format_result(headers=['id', 'name'])
def list_playlists():
    result = control.get_playlists(household_id)
    return result['playlists']
