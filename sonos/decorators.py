import click
import functools
import json
import requests
from click import option
from oauthlib.oauth2 import TokenExpiredError
from tabulate import tabulate

from sonos.config import creds_store
from sonos.settings import REFRESH_TOKEN_URL, SONOS_CLIENT_ID, SONOS_CLIENT_SECRET


def format_result(headers, single=False):
    def decorator_format_result(func):
        @functools.wraps(func)
        def wrapper_format_result(*args, **kwargs):
            def print_json():
                prettified = json.dumps(data, indent=2, sort_keys=True)
                click.echo(prettified)

            def print_table():
                table_data = [data] if single else data
                rows = [[row[header] for header in headers] for row in table_data]
                click.echo(tabulate(rows, headers=headers))

            if "output" in kwargs:
                output = kwargs["output"]
                del kwargs["output"]
            else:
                output = "table"

            data = func(*args, **kwargs)
            if output == "json":
                print_json()
            else:
                print_table()

        return wrapper_format_result

    return decorator_format_result


def output_option(*args, **kwargs):
    def decorator_output_option(func):
        kwargs.setdefault("default", "table")
        return option(
            *(
                args
                or (
                    "--output",
                    "-o",
                )
            ),
            **kwargs
        )(func)

    return decorator_output_option


def login_required(func):
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if creds_store.get_access_token() is None:
            click.echo("Not logged in! Run `sonos login` first.")
            return None
        return func(*args, **kwargs)

    return wrapper_login_required


def config_required(func):
    @functools.wraps(func)
    def wrapper_config_required(*args, **kwargs):
        if SONOS_CLIENT_ID is None or SONOS_CLIENT_SECRET is None:
            click.echo(
                "Not configured. "
                "Run `sonos config` or set environment variables "
                + "SONOS_CLIENT_ID and SONOS_CLIENT_SECRET."
            )
            return None
        return func(*args, **kwargs)

    return wrapper_config_required


def auto_refresh_token(client):
    def decorator_auto_refresh_token(func):
        @functools.wraps(func)
        def wrapper_auto_refresh_token(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except TokenExpiredError:
                token = client.refresh_token(
                    REFRESH_TOKEN_URL,
                    auth=requests.auth.HTTPBasicAuth(
                        SONOS_CLIENT_ID, SONOS_CLIENT_SECRET
                    ),
                )
                client.token = token
                creds_store.save_access_token(token)
                return func(*args, **kwargs)

        return wrapper_auto_refresh_token

    return decorator_auto_refresh_token
