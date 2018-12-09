import functools
import json

import click
from tabulate import tabulate


def format_result(headers):
    def decorator_format_result(func):
        @functools.wraps(func)
        def wrapper_format_result(*args, **kwargs):
            def print_json():
                prettified = json.dumps(data, indent=2, sort_keys=True)
                click.echo(prettified)

            def print_table():
                rows = [[group[header] for header in headers] for group in data]
                click.echo(tabulate(rows, headers=headers))

            if 'output' in kwargs:
                output = kwargs['output']
                del kwargs['output']
            else:
                output = 'table'

            data = func(*args, **kwargs)
            if output == 'json':
                print_json()
            else:
                print_table()

        return wrapper_format_result

    return decorator_format_result
