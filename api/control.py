from http import HTTPStatus

from requests_oauthlib import OAuth2Session

from auth import get_access_token
from config import CLIENT_ID, SONOS_CONTROL_API_BASE_URL

token = get_access_token()
client = OAuth2Session(CLIENT_ID, token=token)


def _url(path):
    return SONOS_CONTROL_API_BASE_URL + path


def _json_or_none(response):
    if response.status_code == HTTPStatus.OK:
        return response.json()
    else:
        return None


def get_households():
    response = client.get(_url('/households'))
    return _json_or_none(response)


def get_groups(household_Id):
    response = client.get(_url(f'/households/{household_Id}/groups'))
    return _json_or_none(response)
