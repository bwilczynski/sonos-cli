import click

from api import control
from auth import login_required
from decorators import format_result
from groups.active_group_store import save_active_group
from households import get_active_household


@click.group()
def groups():
    pass


@groups.command('list')
@click.option('--output', '-o', default='table')
@login_required
@format_result(headers=['coordinatorId', 'id', 'name', 'playbackState'])
def list_groups():
    result = get_groups()
    return result['groups']


@groups.command('use')
@login_required
def use_group():
    result = get_groups()['groups']
    group_names = [group['name'] for group in result]

    for index, name in enumerate(group_names):
        click.echo(f'{index + 1}: {name}')

    number = click.prompt('Which group do you want to use', type=int, default=1)
    if 0 <= number - 1 < len(result):
        selected_group = result[number - 1]
        save_active_group(selected_group['id'])
        click.echo(f'Selected group: {selected_group["name"]}')
    else:
        click.echo('Index out of range.')


def get_groups():
    household_id = get_active_household()
    return control.get_groups(household_id)
