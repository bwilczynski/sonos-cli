import functools

import requests
from oauthlib.oauth2 import TokenExpiredError

from auth import save_access_token
from config import CLIENT_ID, CLIENT_SECRET, SONOS_AUTH_API_BASE_URL

REFRESH_TOKEN_URL = f'{SONOS_AUTH_API_BASE_URL}/login/v3/oauth/access'


def auto_refresh_token(client):
    def decorator_auto_refresh_token(func):
        @functools.wraps(func)
        def wrapper_auto_refresh_token(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except TokenExpiredError:
                token = client.refresh_token(REFRESH_TOKEN_URL,
                                             auth=requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET))
                client.token = token
                save_access_token(token)
                return func(*args, **kwargs)

        return wrapper_auto_refresh_token

    return decorator_auto_refresh_token
