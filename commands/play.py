import click

from api import control
from auth import login_required
from config.active_group_store import get_active_group


@click.command()
@login_required
def play():
    group_id = get_active_group()
    control.play(group_id)
