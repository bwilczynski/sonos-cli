from requests_oauthlib import OAuth2Session

from config import CLIENT_ID, CLIENT_SECRET, SONOS_AUTH_API_BASE_URL

REDIRECT_URL = 'https://haa5mxcg4k.execute-api.eu-west-1.amazonaws.com/default/authorized'
AUTH_URL = f'{SONOS_AUTH_API_BASE_URL}/login/v3/oauth'
ACCESS_TOKEN_URL = f'{SONOS_AUTH_API_BASE_URL}/login/v3/oauth/access'

scope = ['playback-control-all']
client = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URL, scope=scope)


def login():
    return client.authorization_url(AUTH_URL)


def get_access_token(code):
    return client.fetch_token(ACCESS_TOKEN_URL, code=code, username=CLIENT_ID, password=CLIENT_SECRET)
