import click

from sonos.api import control
from sonos.config import active_group_store
from sonos.decorators import output_option, format_result, login_required


@click.command()
@login_required
@output_option()
@format_result(
    headers=["playbackState", "positionMillis", "previousPositionMillis"], single=True
)
def status():
    group_id = active_group_store.get_active_group()
    return control.status(group_id)
