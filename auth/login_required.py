import functools

import click

from config import creds_store


def login_required(func):
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if creds_store.get_access_token() is None:
            click.echo('Not logged in! Run `sonos-cli login` first.')
            return None
        return func(*args, **kwargs)
    return wrapper_login_required
