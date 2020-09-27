from requests_oauthlib import OAuth2Session

from sonos.settings import (
    SONOS_CLIENT_ID,
    SONOS_CLIENT_SECRET,
    CLIENT_REDIRECT_URL,
    AUTH_URL,
    ACCESS_TOKEN_URL,
    CLIENT_SCOPE,
)

client = OAuth2Session(
    SONOS_CLIENT_ID, redirect_uri=CLIENT_REDIRECT_URL, scope=CLIENT_SCOPE
)


def login():
    return client.authorization_url(AUTH_URL)


def get_access_token(code):
    return client.fetch_token(
        ACCESS_TOKEN_URL,
        code=code,
        username=SONOS_CLIENT_ID,
        password=SONOS_CLIENT_SECRET,
        client_secret=SONOS_CLIENT_SECRET,
    )
