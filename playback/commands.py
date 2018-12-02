import click

from api import control
from groups import get_active_group


@click.group()
def playback():
    pass


@playback.command()
def play():
    group_id = get_active_group()
    control.play(group_id)


@playback.command()
def pause():
    group_id = get_active_group()
    control.pause(group_id)
