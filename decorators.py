import functools
import json

import click
from click import option
from tabulate import tabulate


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


def output_option(*args, **kwargs):
    def decorator_output_option(func):
        kwargs.setdefault('default', 'table')
        return option(*(args or ('--output', '-o',)), **kwargs)(func)

    return decorator_output_option
