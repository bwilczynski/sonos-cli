import click

from api import control
from config.active_group_store import get_active_group
from decorators import output_option, format_result, login_required


@click.command()
@login_required
@output_option()
@format_result(headers=['playbackState', 'positionMillis', 'previousPositionMillis'], single=True)
def status():
    group_id = get_active_group()
    return control.status(group_id)
