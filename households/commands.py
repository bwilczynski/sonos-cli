import json

import click
from requests_oauthlib import OAuth2Session

from auth import get_access_token
from config import CLIENT_ID, SONOS_CONTROL_API_BASE_URL


@click.group()
def households():
    pass


@households.command('list')
def list_households():
    token = get_access_token()
    client = OAuth2Session(CLIENT_ID, token=token)
    result = client.get(f'{SONOS_CONTROL_API_BASE_URL}/households').json()
    print(json.dumps(result))
