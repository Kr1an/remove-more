from utils.helpers import clean_path
from utils.managers import bin_config_manager
from utils.managers import user_config_manager


def copy_bin(path, options):
    try:
        return 0
    except Exception as e:
        print(e)
        return 1


def move_bin(path, options):
    try:
        return 0
    except Exception as e:
        print(e)
        return 1


def create_bin(path, options):
    try:
        return 0
    except Exception as e:
        print(e)
        return 1


def empty_bin(options):
    try:
        bin_location = user_config_manager.get_property('bin_path')
        clean_path.delete(bin_location)
        bin_config_manager.set_property('history', [])
        return 0
    except Exception as e:
        print(e)
        return 1
