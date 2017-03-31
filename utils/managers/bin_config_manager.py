"""User Config Manager

Module offer access with both read/write modes to user configuration file.
This config manager stands after ApplicationConfigurationFile in hierarchy
of config managers

Example:
    user_config_manager.get_property('name.short')

According to fact, that almost all functionality stands on
property_reader, property_writer. Read documentation of this modules to
understand how UserConfigManager works.

"""
import json
import os

from utils.helpers import property_reader, property_writer
from utils.managers import app_config_manager
from utils.managers import user_config_manager
from utils.helpers import clean_path
from setting import DEFAULT_CONFIGS


def history_get(bin_name, options=None):
    for history_item in get_property('history'):
        if history_item['bin_name'] == bin_name:
            return history_item
    return None


def history_empty(options=None):
    for history_item in get_property('history'):
        history_del(history_item['bin_name'])


def history_add(src, options=None):
    history_item = {
        'src_dir': os.path.dirname(src),
        'bin_name': os.path.basename(src)
    }
    set_property('history', get_property('history') + [history_item])


def history_del(bin_name, options=None):
    set_property(
        'history',
        [i for i in get_property('history') if i['bin_name'] != bin_name]
    )


def _get_config_path():
    """Get Config Path Function.

    Do not use this function outside of this module.

    Returns:
        String value of file path.
        None if some exception occupies.

    """
    return app_config_manager.get_property('bin_config.path')


def get_property(search_query):
    """Get Property Function.

    Function to access config file in read mode.

    Example:
        user_config_manager.get_property('name.short')

    """
    config = _get_config()
    return property_reader.get_property(config, search_query)


def initialize():
    """Initialize function.

    Function to initialize app_config.json while installing
    programme. Add custom values to default config.

    """
    _set_default_config()
    _set_properties([])


def _set_config(config):
    """Set Config Function.

    Do not use this function outside of this module.

    Attributes:
        config: config dict to set as a app_config

    Returns:
        Boolean that shows if config was changed.

    """
    try:
        config_path = _get_config_path()
        if config_path is None:
            return None

        json_app_config_file = open(config_path, 'w')
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
        config_path = _get_config_path()
        if config_path is None:
            return None

        json_app_config_file = open(config_path, 'r')
        config = json.load(json_app_config_file)
        return config
    except Exception as e:
        print(e)
        return None


def set_property(search_query, value):
    """Set Property Function.

    Function to access config file in write mode

    Example:
        user_config_manager.set_property('name.short', False)

    """
    config = _get_config()
    config = property_writer.set_property(config, search_query, value)

    if config is None:
        return False

    return _set_config(config)


def _set_default_config():
    """Set Default Config Function.

    Do not use this function outside of this module.

    Set config file with default value
    from module setting.DEFAULT_CONFIGS(APP_CONFIG).

    Returns:
        Boolean that shows if config was changed.

    """
    return _set_config(DEFAULT_CONFIGS.BIN_CONFIG)


def _set_properties(props):
    """Set Properties Function.

    Do not use this function outside of this module.

    Attributes:
        props stands for properties. it is a list of properties aliased while
        config initialization.

    """
    for prop in props:
        set_property(prop['key'], prop['value'])

