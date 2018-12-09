import click

from api import control
from auth import login_required
from config.active_group_store import get_active_group
from decorators import output_option, format_result


@click.command()
@login_required
@output_option()
@format_result(headers=['playbackState', 'positionMillis', 'previousPositionMillis'], single=True)
def status():
    group_id = get_active_group()
    return control.status(group_id)
