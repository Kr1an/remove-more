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
import glob

from utils.helpers import clean_path
from utils.managers import user_config_manager, bin_config_manager


def delete(paths, options):
    """Copy Function

    Function allow copy bin folder by path.

    Parameters:
        path: where to copy.
        options: list of copy politics.

    Returns:
        value: 0 - successful, 1 - fail.

    """
    try:
        del_paths = _get_del_paths(paths, options)
        if 'with_no_bin' not in options['mods']:
            _copy_to_bin(del_paths)
        _delete(del_paths)
        return 0
    except Exception as e:
        print(e)
        return 1


def _copy_to_bin(paths):
    """Copy Function

    Function allow copy bin folder by path.

    Parameters:
        path: where to copy.
        options: list of copy politics.

    Returns:
        value: 0 - successful, 1 - fail.

    """
    for path in paths:
        clean_path.copy(path, user_config_manager.get_property('bin_path'))
        bin_config_manager.history_add(path)


def _get_del_paths(paths, options):
    """Copy Function

    Function allow copy bin folder by path.

    Parameters:
        path: where to copy.
        options: list of copy politics.

    Returns:
        value: 0 - successful, 1 - fail.

    """
    deleting_list = set([val for path in paths for val in glob.glob(path)])
    deleting_list = [os.path.abspath(rel_path) for rel_path in deleting_list]
    return deleting_list


def _delete(paths):
    """Copy Function

    Function allow copy bin folder by path.

    Parameters:
        path: where to copy.
        options: list of copy politics.

    Returns:
        value: 0 - successful, 1 - fail.

    """
    for path in paths:
        clean_path.delete(path)
