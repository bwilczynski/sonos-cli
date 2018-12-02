import click

from api import control
from auth import login_required
from households.active_household_store import save_active_household


@click.group()
def households():
    pass


@households.command('list')
@login_required
def list_households():
    result = control.get_households()
    print_households(result)


@households.command('use')
def use_household():
    sonos_households = control.get_households()['households']
    household_names = [household['id'] for household in sonos_households]

    for index, name in enumerate(household_names):
        click.echo(f'{index + 1}: {name}')

    number = click.prompt('Which household do you want to use', type=int, default=1)
    if 0 <= number - 1 < len(sonos_households):
        selected_household = household_names[number - 1]
        save_active_household(selected_household)
        click.echo(f'Selected household: {selected_household}')
    else:
        click.echo('Index out of range.')


def print_households(data):
    res = [household['id'] for household in data['households']]
    for h in res:
        click.echo(h)
