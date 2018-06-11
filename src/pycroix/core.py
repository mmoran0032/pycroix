

import contextlib

import matplotlib

from .palettes import lacroix_palettes


def available():
    """
    Get list of all available LaCroix flavors
    """
    return list(lacroix_palettes.keys())


@contextlib.contextmanager
def context(style, after_reset=False):
    """
    Context manager for using style settings temporarily

    Parameters
    ----------
    style : str, dict, or list
        A style specification. Valid options are:
        +------+-------------------------------------------------------------+
        | str  | The name of a style or a path/URL to a style file. For a    |
        |      | list of available style names, see `style.available`.       |
        +------+-------------------------------------------------------------+
        | dict | Dictionary with valid key/value pairs for                   |
        |      | `matplotlib.rcParams`.                                      |
        +------+-------------------------------------------------------------+
        | list | A list of style specifiers (str or dict) applied from first |
        |      | to last in the list.                                        |
        +------+-------------------------------------------------------------+
    after_reset : bool
        If True, apply style after resetting settings to their defaults;
        otherwise, apply style on top of the current settings.
    """
    with matplotlib.rc_context():
        if after_reset:
            matplotlib.rcdefaults()
        raise NotImplementedError('finish writing')
        yield
