# Sonos command-line interface

Control your Sonos players from command-line. Uses [Sonos Control API](https://developer.sonos.com/reference/control-api/) to control Sonos groups.

## Usage

```bash
$ sonos [OPTIONS] COMMAND [ARGS]
```

### Get Started

[Setup integration](https://developer.sonos.com/build/direct-control/authorize/) with Sonos API and set the following environment variables before running `sonos`:

```bash
export CLIENT_ID={YOUR_CLIENT_ID}
export CLIENT_SECRET={YOUR_CLIENT_SECRET}
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

Get information from your Sonos:

```bash
$ sonos get [groups | households | playlists | tracks]
```

Control playback:

```bash
$ sonos play
$ sonos pause
$ sonos next
$ sonos prev
```

Set active group / household:

```bash
set [group | household]
```

Get playback status:

```bash
$ status
```


