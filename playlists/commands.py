import json

import click
from tabulate import tabulate

from api import control
from auth import login_required
from households import get_active_household

household_id = get_active_household()


@click.group()
def playlists():
    pass


@playlists.command('list')
@click.option('--output', '-o', default='table')
@login_required
def list_playlists(output):
    result = control.get_playlists(household_id)
    print_playlists_json(result) if output == 'json' else print_playlists_table(result)


def print_playlists_json(data):
    prettified = json.dumps(data, indent=2, sort_keys=True)
    click.echo(prettified)


def print_playlists_table(data):
    headers = ['id', 'name']
    rows = [[group[header] for header in headers] for group in data['playlists']]
    click.echo(tabulate(rows, headers=headers))
