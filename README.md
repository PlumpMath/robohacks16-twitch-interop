# robohacks16-irc-client
Contribution of Dronolab team to Robohacks 2016

This project is the intermediary between our hovercraft and Twitch. Basically
it's a script that handle IRC requests with Twitch in order to transmit them to
the hovercraft (using a raspberry pi). We've got a few commands to pilot the
hovercraft.

## Requirements

You only need to have Python 3.x. We are using the native Sockets to achieve our
 tasks.

## Usage

```shell
python3 TwitchIRCClient.py
```

All configurations values are hard-coded but you can easily change them.


## License

MIT (see LICENSE file)
