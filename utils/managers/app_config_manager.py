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
    config = _get_config()
    return property_reader.get_property(config, search_query)


def initialize():
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
    try:
        json_app_config_file = open(APP_CONFIG_FILE_PATH, 'w')
        json_app_config_file.write(json.dumps(config, indent=4))
        return True
    except Exception as e:
        print(e)
        return False


def _get_config():
    try:
        json_app_config_file = open(APP_CONFIG_FILE_PATH, 'r')
        config = json.load(json_app_config_file)
        return config
    except Exception as e:
        print(e)
        return None


def set_property(search_query, value):
    config = _get_config()
    config = property_writer.set_property(config, search_query, value)

    if config is None:
        return None

    return _set_config(config)


def _set_default_config():
    _set_config(DEFAULT_CONFIGS.APP_CONFIG)


def _set_properties(props):
    for prop in props:
        set_property(prop['key'], prop['value'])
