import click

from api.control import get_group_volume, set_group_volume
from config.active_group_store import get_active_group


@click.command()
@click.argument('value', required=False)
def volume(value):
    group_id = get_active_group()
    if value:
        set_group_volume(group_id, value)
    else:
        result = get_group_volume(group_id)
        click.echo(result['volume'])
