import click

from api import control
from groups import get_active_group

group_id = get_active_group()


@click.group()
def playback():
    pass


@playback.command()
def play():
    control.play(group_id)


@playback.command()
def pause():
    control.pause(group_id)


@playback.command()
def next():
    control.skip_to_next_track(group_id)


@playback.command()
def prev():
    control.skip_to_previous_track(group_id)
