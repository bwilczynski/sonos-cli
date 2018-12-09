import click

from api import control
from auth import login_required
from groups import get_active_group

group_id = get_active_group()


@click.group()
def playback():
    pass


@playback.command()
@login_required
def play():
    control.play(group_id)


@playback.command()
@login_required
def pause():
    control.pause(group_id)


@playback.command()
@login_required
def next():
    control.skip_to_next_track(group_id)


@playback.command()
@login_required
def prev():
    control.skip_to_previous_track(group_id)
