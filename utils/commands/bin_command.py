"""Bin Command Module.

Module offers possibility to work with bin structure.
Copy, Move, Empty it.

Example:
    bin_command.move_bin(path, options)

Todo:
    * add option upgrade with different politics.
    * write unittests
"""
import os

from utils.helpers import clean_path
from utils.managers import bin_config_manager
from utils.managers import user_config_manager

from setting.DEFAULT_CONFIGS import ERROR_MESSAGES


def copy_bin(path, options=None):
    """Copy Function

    Function allow copy bin folder by path.

    Parameters:
        path: where to copy.
        options: list of copy politics.

    Returns:
        value: 0 - successful, 1 - fail.

    """
    try:
        clean_path.copy(
            user_config_manager.get_property('bin_path'),
            os.path.abspath(path)
        )
        return 0
    except Exception as e:
        print(e)
        return 1


def move_bin(path, options=None):
    """Move Function

    Function allow move bin folder by path with 
    bin history changes.

    Parameters:
        path: where to move.
        options: list of copy politics.

    Returns:
        value: 0 - successful, 1 - fail.

    """
    try:
        clean_path.move(
            user_config_manager.get_property('bin_path'),
            os.path.abspath(path)
        )
        user_config_manager.set_property(
            'bin_path',
            os.path.abspath(path)
        )
        return 0
    except Exception as e:
        print(e)
        return 1


def create_bin(path, options=None):
    """Create Function

        Function allow to create bin in new location with empty bin.
        Previous bin location is not deleter.

        Parameters:
            path: where to create.
            options: list of copy politics.

        Returns:
            value: 0 - successful, 1 - fail.

        """
    try:
        user_config_manager.set_property(
            'bin_path',
            os.path.abspath(path)
        )
        bin_config_manager.history_empty()
        os.mkdir(user_config_manager.get_property('bin_path'))
        return 0
    except Exception as e:
        print(e)
        return 1


def empty_bin(options=None):
    """Copy Function

    Function allow to empty bin folder and history too.

    Parameters:
        options: list of copy politics.

    Returns:
        value: 0 - successful, 1 - fail.

    """
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


def get_bin_path(options=None):
    """Copy Function

    Function allow to empty bin folder and history too.

    Parameters:
        options: list of copy politics.

    Returns:
        value: 0 - successful, 1 - fail.

    """
    try:
        bin_path = user_config_manager.get_property('bin_path')
        if bin_path:
            print(bin_path)
        else:
            print(ERROR_MESSAGES['bin_not_exists'])
        return 0
    except Exception as e:
        print(e)
        return 1
