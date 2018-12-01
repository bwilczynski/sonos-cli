import json
import os

ACCESS_TOKEN_FILE = 'access_token.json'


def _get_config_dir():
    return os.path.expanduser(os.path.join('~', '.sonos-cli'))


def _get_access_token_file():
    return os.path.join(_get_config_dir(), ACCESS_TOKEN_FILE)


def save_access_token(data):
    token_file = _get_access_token_file()
    os.makedirs(os.path.dirname(token_file), exist_ok=True)
    with os.fdopen(os.open(token_file, os.O_RDWR | os.O_CREAT | os.O_TRUNC, 0o600),
                   'w+') as file:
        json.dump(data, file)


def get_access_token():
    token_file = _get_access_token_file()
    with open(token_file, 'rb') as file:
        return json.load(file)
