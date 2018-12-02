import json

import click
from requests_oauthlib import OAuth2Session
from tabulate import tabulate

from auth import get_access_token, login_required
from config import CLIENT_ID, SONOS_CONTROL_API_BASE_URL
from households import get_active_household


@click.group()
def groups():
    pass


@groups.command('list')
@click.option('--output', '-o', default='table')
@login_required
def list_groups(output):
    household_id = get_active_household()

    token = get_access_token()
    client = OAuth2Session(CLIENT_ID, token=token)
    result = client.get(f'{SONOS_CONTROL_API_BASE_URL}/households/{household_id}/groups').json()
    print_groups_json(result) if output == 'json' else print_groups_table(result)


def print_groups_json(data):
    prettified = json.dumps(data, indent=2, sort_keys=True)
    click.echo(prettified)


def print_groups_table(data):
    headers = ['id', 'name', 'playbackState']
    rows = [[group[header] for header in headers] for group in data['groups']]
    click.echo(tabulate(rows, headers=headers))
