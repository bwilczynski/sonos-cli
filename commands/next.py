import click

from api import control
from config.active_group_store import get_active_group
from decorators import login_required


@click.command()
@login_required
def next():
    group_id = get_active_group()
    control.skip_to_next_track(group_id)
