import json

import click
from tabulate import tabulate

from api import control
from auth import login_required
from groups.active_group_store import save_active_group
from households import get_active_household


@click.group()
def groups():
    pass


@groups.command('list')
@click.option('--output', '-o', default='table')
@login_required
def list_groups(output):
    result = get_groups()
    print_groups_json(result) if output == 'json' else print_groups_table(result)


@groups.command('use')
def use_group():
    sonos_groups = get_groups()['groups']
    group_names = [group['name'] for group in sonos_groups]

    for index, name in enumerate(group_names):
        click.echo(f'{index + 1}: {name}')

    number = click.prompt('Which group do you want to use', type=int)
    if 0 <= number < len(sonos_groups):
        selected_group = sonos_groups[number]
        save_active_group(selected_group['id'])
        click.echo(f'Selected group: {selected_group["name"]}')
    else:
        click.echo('Index out of range.')


def get_groups():
    household_id = get_active_household()
    return control.get_groups(household_id)


def print_groups_json(data):
    prettified = json.dumps(data, indent=2, sort_keys=True)
    click.echo(prettified)


def print_groups_table(data):
    headers = ['id', 'name', 'playbackState']
    rows = [[group[header] for header in headers] for group in data['groups']]
    click.echo(tabulate(rows, headers=headers))
