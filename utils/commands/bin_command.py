import os

from utils.helpers import clean_path
from utils.managers import bin_config_manager
from utils.managers import user_config_manager


def copy_bin(path, options):
    try:
        clean_path.copy(user_config_manager.get_property('bin_path'), path)
        return 0
    except Exception as e:
        print(e)
        return 1


def move_bin(path, options):
    try:
        clean_path.move(user_config_manager.get_property('bin_path'), path)
        user_config_manager.set_property('bin_path', path)
        return 0
    except Exception as e:
        print(e)
        return 1


def create_bin(path, options):
    try:
        user_config_manager.set_property(
            'bin_path',
            path
        )
        bin_config_manager.history_empty()
        os.mkdir(user_config_manager.get_property('bin_path'))
        return 0
    except Exception as e:
        print(e)
        return 1


def empty_bin(options):
    try:
        for history_item in bin_config_manager.get_property('history'):
            bin_config_manager.history_del(history_item['bin_name'])
            clean_path.delete(
                user_config_manager.get_property('bin_path'),
                history_item['bin_name']
            )
        return 0
    except Exception as e:
        print(e)
        return 1
