from requests_oauthlib import OAuth2Session

from config.creds_store import get_access_token
from decorators import auto_refresh_token
from settings import SONOS_CLIENT_ID, SONOS_CONTROL_API_BASE_URL

token = get_access_token()
client = OAuth2Session(SONOS_CLIENT_ID, token=token)


def _url(path):
    return SONOS_CONTROL_API_BASE_URL + path


def _playback_url(group_id, path=None):
    return _url(f'/groups/{group_id}/playback') + (path or '')


def _json(response):
    response.raise_for_status()
    return response.json()


def get_households():
    response = client.get(_url('/households'))
    return _json(response)


@auto_refresh_token(client=client)
def get_groups(household_id):
    response = client.get(_url(f'/households/{household_id}/groups'))
    return _json(response)


def status(group_id):
    response = client.get(_playback_url(group_id))
    return _json(response)


def play(group_id):
    response = client.post(_playback_url(group_id, '/play'))
    return _json(response)


def pause(group_id):
    response = client.post(_playback_url(group_id, '/pause'))
    return _json(response)


def skip_to_next_track(group_id):
    response = client.post(_playback_url(group_id, '/skipToNextTrack'))
    return _json(response)


def skip_to_previous_track(group_id):
    response = client.post(_playback_url(group_id, '/skipToPreviousTrack'))
    return _json(response)


def get_playlists(household_id):
    response = client.get(_url(f'/households/{household_id}/playlists'))
    return _json(response)


def get_tracks(household_id, playlist_id):
    response = client.post(_url(f'/households/{household_id}/playlists/getPlaylist'), json={'playlistId': playlist_id})
    return _json(response)


def load_playlist(group_id, playlist_id, play_on_completion=None):
    response = client.post(_url(f'/groups/{group_id}/playlists'),
                           json={'playlistId': playlist_id, 'playOnCompletion': play_on_completion})
    return _json(response)
