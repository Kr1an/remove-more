"""App Config Manager

Module offer access with both read/write modes to app configuration file.
This config manager stands in the top of config managers hierarchy.

Example:
    app_config_manager.set_property('name.short', ')

According to fact, that almost all functionality stands on
property_reader, property_writer. Read documentation of this modules to
understand how AppConfigManager works.

"""
import os
import json

from utils.helpers import property_reader, property_writer
from setting import DEFAULT_CONFIGS

APP_CONFIG_FILE_PATH = \
    os.path.abspath(
        os.path.join(
            __file__,
            '..',
            '..',
            '..',
            'setting',
            'app_config.json')
    )


def get_property(search_query):
    """Get Property Function.

    Function to access config file in read mode.

    Example:
        app_config_manager.get_property('user_config.use_custom')

    """
    config = _get_config()
    return property_reader.get_property(config, search_query)


def initialize():
    """Initialize function.

    Function to initialize app_config.json while installing
    programme. Add custom values to default config.

    """
    _set_default_config()
    _set_properties([
        {
            'key': 'user_config.use_custom',
            'value': False
        },
        {
            'key': 'user_config.path.default',
            'value': os.path.join(
                os.path.dirname(APP_CONFIG_FILE_PATH),
                'user_config_default.json'
            )
        },
        {
            'key': 'user_config.path.custom',
            'value': os.path.join(
                os.path.dirname(APP_CONFIG_FILE_PATH),
                'user_config_custom.json'
            )
        }
    ])


def _set_config(config):
    """Set Config Function.

    Do not use this function outside of this module.

    Attributes:
        config: config dict to set as a app_config

    Returns:
        Boolean that shows if config was changed.

    """
    try:
        json_app_config_file = open(APP_CONFIG_FILE_PATH, 'w')
        json_app_config_file.write(json.dumps(config, indent=4))
        return True
    except Exception as e:
        print(e)
        return False


def _get_config():
    """Get Config Function.

    Do not use this function outside of this module.

    Returns:
        Dict object if operation of getting config was successful.
        Otherwise 'None'

    """
    try:
        json_app_config_file = open(APP_CONFIG_FILE_PATH, 'r')
        config = json.load(json_app_config_file)
        return config
    except Exception as e:
        print(e)
        return None


def set_property(search_query, value):
    """Set Property Function.

    Function to access config file in write mode

    Example:
        app_config_manager.set_property('user_config.use_custom', False)

    """
    config = _get_config()
    config = property_writer.set_property(config, search_query, value)

    if config is None:
        return None

    return _set_config(config)


def _set_default_config():
    """Set Default Config Function.

    Do not use this function outside of this module.

    Set config file with default value
    from module setting.DEFAULT_CONFIGS(APP_CONFIG).

    Returns:
        Boolean that shows if config was changed.

    """
    return _set_config(DEFAULT_CONFIGS.APP_CONFIG)


def _set_properties(props):
    """Set Properties Function.

    Do not use this function outside of this module.

    Attributes:
        props stands for properties. it is a list of properties aliased while
        config initialization.

    """
    for prop in props:
        set_property(prop['key'], prop['value'])
