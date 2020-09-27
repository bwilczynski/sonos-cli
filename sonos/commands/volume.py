import click

from sonos.api.control import (
    get_group_volume,
    set_group_volume,
    set_group_relative_volume,
)
from sonos.config import active_group_store


@click.command()
@click.argument("value", required=False)
def volume(value):
    group_id = active_group_store.get_active_group()
    if value:
        if value[0] in ("+", "-"):
            set_group_relative_volume(group_id, value)
        else:
            set_group_volume(group_id, value)
    else:
        result = get_group_volume(group_id)
        click.echo(result["volume"])
