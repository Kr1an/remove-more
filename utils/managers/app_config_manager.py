import os
import json

from utils.helpers import property_reader

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
    try:
        with open(APP_CONFIG_FILE_PATH, 'r') as json_app_config_file:
            app_config = json.load(json_app_config_file)
    except:
        return None

    return property_reader.get_property(app_config, search_query)


def initialize():
    pass

def setert(property):
    pass