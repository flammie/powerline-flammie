# vim:fileencoding=utf-8:noet
import os

from powerline.theme import requires_segment_info

# os.geteuid is not available on windows
_geteuid = getattr(os, 'geteuid', lambda: 1)


@requires_segment_info
def usersigil(pl, segment_info):
    '''Return the current user symbol like $#.

    Highlights the user with the ``superuser`` if the effective user ID is 0.

    Highlight groups used: ``superuser`` or ``user``. It is recommended to
    define all highlight groups.
    '''
    euid = _geteuid()
    return [{
        'contents': '$' if euid != 0 else '#',
        'highlight_groups': ['user'] if euid != 0 else ['superuser',
                                                        'user'],
    }]
