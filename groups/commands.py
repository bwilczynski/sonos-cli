import json

import click
from requests_oauthlib import OAuth2Session

from auth import get_access_token
from config import CLIENT_ID, SONOS_CONTROL_API_BASE_URL
from households import get_active_household


@click.group()
def groups():
    pass


@groups.command('list')
def list_groups():
    household_id = get_active_household()

    token = get_access_token()
    client = OAuth2Session(CLIENT_ID, token=token)
    result = client.get(f'{SONOS_CONTROL_API_BASE_URL}/households/{household_id}/groups').json()
    print_groups(result)


def print_groups(data):
    prettified = json.dumps(data, indent=2, sort_keys=True)
    click.echo(prettified)
