import click
from requests_oauthlib import OAuth2Session

from auth import get_access_token
from config import CLIENT_ID, SONOS_CONTROL_API_BASE_URL
from households import active_household_store


@click.group()
def households():
    pass


@households.command('list')
def list_households():
    token = get_access_token()
    client = OAuth2Session(CLIENT_ID, token=token)
    result = client.get(f'{SONOS_CONTROL_API_BASE_URL}/households').json()
    print_households(result)


@households.command('use')
@click.argument('household_id')
def use_household(household_id):
    active_household_store.save_active_household(household_id)


def print_households(data):
    res = [household["id"] for household in data["households"]]
    for h in res:
        click.echo(h)
