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

from setting.DEFAULT_CONFIGS import INFO_MESSAGES, HISTORY_COPY_NAME_FORMAT

from utils.helpers.log_helper import  get_log

from utils.helpers import ascii_bar

from utils.helpers.confirmer import confirm_question


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
        # Check if command run in confirm mod and if it's so, ask
        # user about activity confirmation.
        if not confirm_question(
            "Try to delete: \n{}\n".format(
                "\n".join(map(lambda x: '--' + x, del_paths))
            ),
            "no", options
        ):
            return 1

        # Check if command run in dry mode and if so skip main management
        # operation and only print info
        if not bin_config_manager.is_dry_mode(options):
            if not options or 'nobin' not in options:
                _copy_to_bin(del_paths, options)
            _delete(del_paths, options)
        # Print info about what was done while operation
        get_log().info(INFO_MESSAGES['delete'].format(
            '\n '.join(del_paths)
        ))
        return 0
    except Exception as e:
        get_log().error(e)
        return 1


def _copy_by_force_way(path, options):
    """Copy By Force Way

    Function allow to delete file/dir... to bin by rename way if name
    collision exists.

    Arguments:
        path: path to source.
        options: list of optional parameters.

    """
    if os.path.exists(
        os.path.join(
            user_config_manager.get_property('bin_path'),
            os.path.basename(path)
        )
    ):
        bin_config_manager.history_del(os.path.basename(path))
        clean_path.delete(
            os.path.join(
                user_config_manager.get_property('bin_path'),
                os.path.basename(path)
            )
        )
    bin_config_manager.history_add(path)
    clean_path.copy(
        path,
        os.path.join(
            user_config_manager.get_property('bin_path'),
            os.path.basename(path)
        ),
        options
    )


def _copy_by_rename_way(path, options):
    """Copy By Renam Way
    
    Function allow to delete file/dir... to bin by rename way if name
    collision exists.
    
    Arguments:
        path: path to source.
        options: list of optional parameters.
    
    """
    src_name = os.path.basename(path)
    src_dir = os.path.dirname(path)
    bin_name = os.path.basename(path)
    if bin_config_manager.history_get(bin_name, options):

        count = 0
        while True:

            tmp_bin_name = HISTORY_COPY_NAME_FORMAT.format(bin_name, count)
            if not bin_config_manager.history_get(tmp_bin_name, options):
                break
            count += 1
        bin_name = tmp_bin_name

    clean_path.copy(
        path, os.path.join(user_config_manager.get_property('bin_path'), bin_name),
        options
    )
    bin_config_manager.history_add(
        {
            'src_name': src_name,
            'src_dir': src_dir,
            'bin_name': bin_name
        },
        options
    )


def _copy_to_bin(paths, options=None):
    """Copy To Bin Function
    
    Do not use this function outside of module.

    Function allow copy bin folder by path.

    Parameters:
        paths: what to copy.
        options: list of copy politics.


    """
    for path in paths:
        if options and 'force' in options:
            _copy_by_force_way(path, options)
        else:
            _copy_by_rename_way(path, options)


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
    # Get paths if it was passed by regex option.
    if options and 'regex' in options:
        deleting_list = _get_paths_from_regex(options['regex'])
    # Get paths otherwise
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
    # Get paths if regex does not have '**'-recursive mark
    if '**' not in regex:
        return glob.glob(regex)
    # Get paths if regex does have '**'
    else:
        path = regex
        # Get First(deepest) possible folder in path
        while not os.path.exists(os.path.abspath(path)) and path != '/':
            path = os.path.dirname(path)

        reg_suffix = os.path.basename(regex)
        paths = []

        # Walk recursive with in found folder and check every file
        # to be equal to reg_suffix
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
    # Go through ecery path and delete it from
    # src location.
    for path in paths:
        clean_path.delete(path, options)
        if os.path.dirname(path) == user_config_manager.get_property('bin_path'):
            bin_config_manager.history_del(os.path.basename(path), options)
        # Print progress of operation
        get_log().info(
            INFO_MESSAGES['progress_del'].format(
                ascii_bar.get_progress_bar(
                    paths.index(path) + 1,
                    len(paths)
                ),
                path
            )
        )
