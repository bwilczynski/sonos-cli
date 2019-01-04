# Sonos command-line interface

Control your Sonos players from command-line. Uses [Sonos Control API](https://developer.sonos.com/reference/control-api/) to control Sonos groups.

## Installation

Using `pip` (requires Python 3):

```sh
pip install sonos-cli
```

## Usage

```bash
$ sonos [OPTIONS] COMMAND [ARGS]
```

### Get Started

[Setup integration](https://developer.sonos.com/build/direct-control/authorize/) with Sonos API 
and run `sonos config` to provide 
your application's Client ID and Client Secret.

Alternatively set the following environment variables before running `sonos`:

```bash
export SONOS_CLIENT_ID={YOUR_CLIENT_ID}
export SONOS_CLIENT_SECRET={YOUR_CLIENT_SECRET}
```

Login to your Sonos service (opens a web browser sending user to Sonos login service):

```bash
$ sonos login
```

Set active household:

```bash
$ sonos set household
```

For usage and help content, pass in the `--help` parameter, for example:

```bash
$ sonos --help
$ sonos get --help
```

### Available commands

#### Get information from your Sonos:

```bash
$ sonos get [groups | households | playlists | tracks]
```

Format displayed result using `--output` option:


```bash
$ sonos get groups --output table

coordinatorId             id                                   name              playbackState
------------------------  -----------------------------------  ----------------  ----------------------
RINCON_B8E937E6D36202100  RINCON_B8E937E6D36202100:23          Bedroom.          PLAYBACK_STATE_PAUSED
RINCON_B8E937E6D40E02100  RINCON_B8E937E6D40E02100:128         Bathroom          PLAYBACK_STATE_IDLE
RINCON_B8E937DA7E6802100  RINCON_B8E937DA7E6802100:17          Bathroom 2.       PLAYBACK_STATE_PAUSED
RINCON_347E5C90FA9502100  RINCON_347E5C90FA9502100:4142323492  Living Room       PLAYBACK_STATE_PLAYING
```

```bash
$ sonos get groups --output json

[
  {
    "coordinatorId": "RINCON_B8E937E6D36202100",
    "id": "RINCON_B8E937E6D36202100:23",
    "name": "Bedroom",
    "playbackState": "PLAYBACK_STATE_PAUSED",
    ...
  }
  ...
}
```

#### Control playback:

```bash
$ sonos play
$ sonos pause
$ sonos next
$ sonos prev
```

#### Set active group / household:

```bash
$ sonos set [group | household]
```

#### Get playback status:

```bash
$ sonos status
```

#### Control group volume

```bash
$ sonos volume
20
```

```bash
$ sonos volume 25
```
