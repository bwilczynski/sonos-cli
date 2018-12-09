import functools

import requests
from oauthlib.oauth2 import TokenExpiredError

from config.creds_store import save_access_token
from settings import SONOS_CLIENT_ID, SONOS_CLIENT_SECRET, REFRESH_TOKEN_URL


def auto_refresh_token(client):
    def decorator_auto_refresh_token(func):
        @functools.wraps(func)
        def wrapper_auto_refresh_token(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except TokenExpiredError:
                token = client.refresh_token(REFRESH_TOKEN_URL,
                                             auth=requests.auth.HTTPBasicAuth(SONOS_CLIENT_ID, SONOS_CLIENT_SECRET))
                client.token = token
                save_access_token(token)
                return func(*args, **kwargs)

        return wrapper_auto_refresh_token

    return decorator_auto_refresh_token
