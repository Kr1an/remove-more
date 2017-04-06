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
    },
    "logger":{
        "name": "main_logger",
        "level": 'DEBUG',
        "formats": {
            'default': "%(message)s",
            'INFO': "%(message)s",
            'WARNING': "%(levelname)s: %(message)s",
            'ERROR': "%(levelname)s: %(message)s: Description: %(pathname)s",
            'CRITICAL': "%(levelname)s: %(message)s: Description: %(pathname)s: %(asctime)s"
        }
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
    },
    {
        "name": "--binpath",
        "shortcut": "-bp",
        "help": "Print absolute path to bin folder",
        "action": "store_true"
    },
    {
        "name": "--regex",
        "shortcut": "-rex",
        "help": "Check specific reg ex path",
        "action": "store"
    },
    {
        "name": "--binprint",
        "shortcut": "-bpr",
        "help": "Prints bin objects file/dir-names.",
        "action": "store_true"
    },
    {
        "name": "--silent",
        "shortcut": "-st",
        "help": "Execute command without output",
        "action": "store_true"
    },
    {
        "name": "--dry",
        "shortcut": "-dr",
        "help": "Execute command doing some real changes",
        "action": "store_true"
    }
]
ERROR_MESSAGES = {
    'bin_not_exists':
        'Bin folder does not exists. '
        'Create one with \'--bincreate=../path_to_bin_folder/..\' command.',
    'app_config_error':
        "Application config is not valid. See --help to find solution.",
    'user_config_error':
        "Application config is not valid. See --help to find solution.",
    'bin_config_error':
        "Application config is not valid. See --help to find solution."
}
INFO_MESSAGES = {
    'bin_restore': 'To restore files from bin. go to bin(use --binpath option)'
                   ' and use --restore option to accomplish your goal.',
    "bin_copy": "Copy bin to {}.",
    "bin_move": "Bin folder was moved to location: {}",
    "bin_empty": "\nBin was cleaned",
    "list_item": "----{};",
    "bin_path": "Bin location: {}",
    "bin_create": "Empty bin was created on path: {}",
    "delete": "Was Deleted: \n {}",
    "restore": "Was Restored: \n {}",
    "progress_res": "{} ... Restore {}",
    "progress_del": "{} ... Delete {}"
}
