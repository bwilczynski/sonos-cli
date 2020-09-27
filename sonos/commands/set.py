import click

from sonos.api import control
from sonos.config import active_group_store, active_household_store
from sonos.decorators import login_required


@click.group()
def set():
    pass


@set.command()
@login_required
def household():
    result = control.get_households()["households"]
    household_names = [household["id"] for household in result]

    index = show_prompt("Which household do you want to use", household_names)
    if index != -1:
        selected_household = household_names[index]
        active_household_store.save_active_household(selected_household)
        click.echo(f"Selected household: {selected_household}")
    else:
        click.echo("Index out of range.")


@set.command()
@login_required
def group():
    household_id = active_household_store.get_active_household()
    result = control.get_groups(household_id)["groups"]
    group_names = [group["name"] for group in result]

    index = show_prompt("Which group do you want to use", group_names)
    if index != -1:
        selected_group = result[index]
        active_group_store.save_active_group(selected_group["id"])
        click.echo(f'Selected group: {selected_group["name"]}')
    else:
        click.echo("Index out of range.")


def show_prompt(message, options):
    for index, name in enumerate(options):
        click.echo(f"{index + 1}: {name}")

    number = click.prompt(message, type=int, default=1)
    index = number - 1
    return index if 0 <= index < len(options) else -1
