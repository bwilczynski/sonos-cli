from requests_oauthlib import OAuth2Session

from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, AUTH_URL, ACCESS_TOKEN_URL, CLIENT_SCOPES

client = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URL, scope=CLIENT_SCOPES)


def login():
    return client.authorization_url(AUTH_URL)


def get_access_token(code):
    return client.fetch_token(ACCESS_TOKEN_URL, code=code, username=CLIENT_ID, password=CLIENT_SECRET)
