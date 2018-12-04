from http import HTTPStatus

from requests_oauthlib import OAuth2Session

from auth import get_access_token
from config import CLIENT_ID, SONOS_CONTROL_API_BASE_URL

token = get_access_token()
client = OAuth2Session(CLIENT_ID, token=token)


class APIException(Exception):
    pass


def _url(path):
    return SONOS_CONTROL_API_BASE_URL + path


def _json(response):
    response.raise_for_status()
    return response.json()


def get_households():
    response = client.get(_url('/households'))
    return _json(response)


def get_groups(household_Id):
    response = client.get(_url(f'/households/{household_Id}/groups'))
    return _json(response)


def play(group_id):
    response = client.post(_url(f'/groups/{group_id}/playback/play'))
    response.raise_for_status()


def pause(group_id):
    response = client.post(_url(f'/groups/{group_id}/playback/pause'))
    response.raise_for_status()


def skip_to_next_track(group_id):
    response = client.post(_url(f'/groups/{group_id}/playback/skipToNextTrack'))
    response.raise_for_status()


def skip_to_previous_track(group_id):
    response = client.post(_url(f'/groups/{group_id}/playback/skipToPreviousTrack'))
    response.raise_for_status()
