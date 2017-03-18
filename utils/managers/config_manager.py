import json

from utils.helpers import property_reader
from utils.managers import app_config_manager as app_settings

#
# !!!config is duplicated!!!
#

config_dup = {
    'name': {
        'short': 'rr',
        'normal': 'RemoveRestore'
    }
}


def get_property(search_query):
    config = load_config()
    return property_reader.get_property(
        config,
        search_query
    )


def load_config():
    if app_settings.get_property('config.use_custom'):
        config_file_path = app_settings.get_property('config.path.default')
    else:
        config_file_path = app_settings.get_property('config.path.custom')

    try:
        with open(config_file_path, 'r') as json_config_file:
            config = json.load(json_config_file)
            return config
    except:
        return None

def initialize():
    pass