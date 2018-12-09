import click

from api import control
from auth import login_required
from decorators import format_result
from households.active_household_store import save_active_household


@click.group()
def households():
    pass


@households.command('list')
@click.option('--output', '-o', default='table')
@login_required
@format_result(headers=['id'])
def list_households():
    result = control.get_households()
    return result['households']


@households.command('use')
@login_required
def use_household():
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
