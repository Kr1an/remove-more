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
    "author": "kr1an@hotmail.com"
}

USER_CONFIG = {
    "name": {
        "short": "rr",
        "normal": "RemoveRestore",
    }
}

