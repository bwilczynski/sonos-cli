import click

from api import control
from config.active_group_store import get_active_group
from decorators import login_required


@click.command()
@login_required
def pause():
    group_id = get_active_group()
    control.pause(group_id)
