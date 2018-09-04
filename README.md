# powerline-flammie

Some powerline segments

## Installation

```
sudo cp stuff.py /usr/lib/python3.5/site-packages/powerline-flammie/
sudo mkdir /usr/lib/python3.5/site-packages/powerline-flammie/
```

## Configuration

[My shell
config](//github.com/flammie/dotfiles/master/powerline/themes/shell/test.json):

```json
{
	"segments": {
        "above": [
            {
               "left": [
                    {
                        "function": "powerline.segments.common.net.hostname"
                    },
                    {
                        "function": "powerline.segments.common.env.user"
                    },
                    {
                        "function": "powerline.segments.common.env.virtualenv"
                    },
                    {
                        "function": "powerline.segments.common.vcs.branch"
                    },
                    {
                        "function": "powerline.segments.shell.cwd"
                    }
                ],
                "right": [
                    {
                        "function": "powerline.segments.common.time.date"
                    }
                ]
            }
        ],
        "left": [
            {
                "function": "powerline-flammie.stuff.usersigil"
            }
        ],
        "right": [
            {
                "function": "powerline.segments.shell.last_pipe_status"
            }
        ]
	}
}
```
