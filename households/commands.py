import click

from api import control
from auth import login_required
from households import active_household_store


@click.group()
def households():
    pass


@households.command('list')
@login_required
def list_households():
    result = control.get_households()
    print_households(result)


@households.command('use')
@click.argument('household_id')
def use_household(household_id):
    active_household_store.save_active_household(household_id)


def print_households(data):
    res = [household["id"] for household in data["households"]]
    for h in res:
        click.echo(h)
