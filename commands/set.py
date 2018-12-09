import click

from api import control
from auth import login_required
from config.active_group_store import save_active_group
from config.active_household_store import save_active_household, get_active_household


@click.group()
def set():
    pass


@set.command()
@login_required
def household():
    result = control.get_households()['households']
    household_names = [household['id'] for household in result]

    for index, name in enumerate(household_names):
        click.echo(f'{index + 1}: {name}')

    number = click.prompt('Which household do you want to use', type=int, default=1)
    if 0 <= number - 1 < len(result):
        selected_household = household_names[number - 1]
        save_active_household(selected_household)
        click.echo(f'Selected household: {selected_household}')
    else:
        click.echo('Index out of range.')


@set.command()
@login_required
def group():
    household_id = get_active_household()
    result = control.get_groups(household_id)['groups']
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
