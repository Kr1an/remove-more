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


def delete(paths, options=None):
    """Delete Function

    Function allow to delete file/dirs by paths
    in different mods.

    Parameters:
        paths: where to copy.
        options: list of copy politics.

    Returns:
        value: 0 - successful, 1 - fail.

    """
    try:
        del_paths = _get_del_paths(paths, options)
        if 'with_no_bin' not in options['mods']:
            _copy_to_bin(del_paths, options)
        _delete(del_paths, options)
        return 0
    except Exception as e:
        print(e)
        return 1


def _copy_to_bin(paths, options=None):
    """Copy To Function
    
    Do not use this function outside of module.

    Function allow copy bin folder by path.

    Parameters:
        paths: what to copy.
        options: list of copy politics.


    """
    for path in paths:
        clean_path.copy(
            path, user_config_manager.get_property('bin_path'),
            options
        )
        bin_config_manager.history_add(path, options)


def _get_del_paths(paths, options=None):
    """Copy Function
    
    Do not use this function outside of module.

    Function get paths and find regex in it, expend list and
    return expended array of paths.

    Parameters:
        paths: paths to expend.
        options: list of copy politics.
    
    Returns:
        value: list of valid paths.

    """
    deleting_list = set([val for path in paths for val in glob.glob(path)])
    deleting_list = [os.path.abspath(rel_path) for rel_path in deleting_list]
    return deleting_list


def _delete(paths, options=None):
    """Delete Function
    
    Do not use this function outside of module.

    Function deletes every path of paths.

    Parameters:
        paths: what to delete.
        options: list of delete politics.

    """
    for path in paths:
        clean_path.delete(path, options)
