import json

from utils.helpers import property_reader, property_writer
from utils.managers import app_config_manager
from setting import DEFAULT_CONFIGS


def _get_config_path():
    use_custom_config = app_config_manager.get_property(
        'user_config.use_custom'
    )
    search_query = 'user_config.path.{}'.format(
        'custom' if use_custom_config else 'default'
    )

    return app_config_manager.get_property(search_query)


def get_property(search_query):
    config = _get_config()
    return property_reader.get_property(config, search_query)


def initialize():
    _set_default_config()
    _set_properties([])


def _set_config(config):
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
    config = _get_config()
    config = property_writer.set_property(config, search_query, value)

    if config is None:
        return False

    return _set_config(config)


def _set_default_config():
    _set_config(DEFAULT_CONFIGS.USER_CONFIG)


def _set_properties(props):
    for prop in props:
        set_property(prop['key'], prop['value'])

