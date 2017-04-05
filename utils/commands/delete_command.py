"""Delete Command Module.

Module offers possibility to work with delete functionality.

Example:
    delete_command.delete(path, options)

Todo:
    * add option upgrade with different politics.
    * write unittests
"""
import os
import glob
import fnmatch

import logging


from utils.helpers import clean_path
from utils.managers import user_config_manager, bin_config_manager

from setting.DEFAULT_CONFIGS import INFO_MESSAGES

from utils.helpers.log_helper import  get_log


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
        _copy_to_bin(del_paths, options)
        _delete(del_paths, options)
        get_log().info(INFO_MESSAGES['delete'].format(
            '\n '.join(del_paths)
        ))
        return 0
    except Exception as e:
        get_log().error(e)
        return 1


def _copy_to_bin(paths, options=None):
    """Copy To Bin Function
    
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
    """Get Del Paths
    
    Do not use this function outside of module.

    Function get paths and find regex in it, expend list and
    return expended array of paths.

    Parameters:
        paths: paths to expend.
        options: list of copy politics.
    
    Returns:
        value: list of valid paths.

    """
    if options and 'regex' in options:
        deleting_list = _get_paths_from_regex(options['regex'])
    else:
        deleting_list = set([val for path in paths for val in glob.glob(path)])
    deleting_list = [os.path.abspath(rel_path) for rel_path in deleting_list]
    return deleting_list


def _get_paths_from_regex(regex):
    """Get  Paths From Regex Function.

    Do not use this function outside of module.

    Function get paths and find regex in it, expend list and
    return expended array of paths. The key is that python 2.2-2.7
    does not understand 2 asterics sign(**) in regex, thus, this
    function solves this problem in not very hard way.

    Parameters:
        regex: string with rel/abs path, that could have regex within it. 

    Returns:
        value: list of valid paths.

    """
    if '**' not in regex:
        return glob.glob(regex)
    else:
        path = regex
        while not os.path.exists(os.path.abspath(path)) and path != '/':
            path = os.path.dirname(path)

        reg_suffix = os.path.basename(regex)
        paths = []

        for root, dirs, files in os.walk(os.path.abspath(path)):
            for file in fnmatch.filter(files, reg_suffix):
                paths.append(os.path.join(root, file))

        return paths


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
