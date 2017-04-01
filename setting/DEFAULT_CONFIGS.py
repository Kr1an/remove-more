""" Default configurations module

This module is used as a storage for default configurations state.
Values in this module should not be changed on runtime execution.

Example:
    Usage: from setting import *

Attributes:
    APP_CONFIG: dict of default state for app_config file.
    USER_CONFIG: dict of default state for user_config file.

This module is maintainable, and could be changed and extended.

"""

APP_CONFIG = {
    "name": {
        "short": "rr",
        "normal": "RemoveRestore",
    },
    "supported_platforms": [
        "linux",
        "linux2"
    ],
    "version": "",
    "user_config": {
        "path": {
            "default": "",
            "custom": ""
        },
        "use_custom": False
    },
    "app_location": "",
    "author": "kr1an@hotmail.com",
    "bin_config": {
        "path": ""
    }
}

USER_CONFIG = {
    "bin_path": ""
}

BIN_CONFIG = {
    "history": []
}

ARGS_CONFIG = [
    {
        "name": "--binmove",
        "shortcut": '-bm',
        "help": "Move bin folder to specific location <path>",
        "action": "store"
    },
    {
        "name": "--bincopy",
        "shortcut": '-bcp',
        "help": "Copy bin folder to specific location <path>",
        "action": "store"

    },
    {
        "name": "--bincreate",
        "shortcut": '-bcr',
        "help": "Create clean new bin folder by specific <path>",
        "action": "store"
    },
    {
        "name": "--binempty",
        "shortcut": '-be',
        "help": "Empty bin folder",
        "action": "store_true"

    },
    {
        "name": "--restore",
        "shortcut": "-re",
        "help": "Specify than <paths> is needed to be restored",
        "action": "store_true"
    }
]
