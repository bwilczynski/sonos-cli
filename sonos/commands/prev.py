import click

from sonos.api import control
from sonos.config import active_group_store
from sonos.decorators import login_required


@click.command()
@login_required
def prev():
    group_id = active_group_store.get_active_group()
    control.skip_to_previous_track(group_id)
