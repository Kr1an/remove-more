"""Restore Command Module.

Module offers possibility to work with restore functionality.

Example:
    restore_command.restore(path, options)

Todo:
    * add option upgrade with different politics.
    * write unittests
    
"""
import os
import glob

from utils.helpers import clean_path
from utils.managers import user_config_manager, bin_config_manager

from utils.helpers.log_helper import get_log

from setting.DEFAULT_CONFIGS import INFO_MESSAGES

from utils.helpers import ascii_bar

from utils.helpers.confirmer import confirm_question


def restore(paths, options=None):
    """Restore Function

    Function allow to restore file/dirs by paths
    in different mods.

    Parameters:
        paths: what to restore.
        options: list of restore politics.

    Returns:
        value: 0 - successful, 1 - fail.

    """
    try:

        restore_paths = _get_restore_paths(paths, options)
        if not confirm_question(
            "Try to restore: \n{}\n".format(
                "\n".join(map(lambda x: '--' + x, restore_paths))
            ),
            "no", options
        ):
            return 1

        if not bin_config_manager.is_dry_mode(options):
            _move_from_bin(restore_paths, options)

        get_log().info(
            INFO_MESSAGES['restore'].format('\n '.join(restore_paths))
        )

        return 0
    except Exception as e:
        get_log().error(e)
        return 1


def _move_from_bin(paths, options=None):
    """Copy From Bin Function

    Do not use this function outside of module.

    Function allow copy bin files to destination.

    Parameters:
        paths: what to copy.
        options: list of copy politics.


    """
    for path in paths:
        clean_path.move(
            os.path.join(
                user_config_manager.get_property('bin_path'),
                bin_config_manager.history_get(path, options)['bin_name']
            ),
            os.path.join(
                bin_config_manager.history_get(path, options)['src_dir'],
                bin_config_manager.history_get(path, options)['src_name'],
            ),
            options
        )
        bin_config_manager.history_del(path, options)
        get_log().info(
            INFO_MESSAGES['progress_res'].format(
                ascii_bar.get_progress_bar(
                    paths.index(path) + 1,
                    len(paths)
                ),
                path
            )
        )


def _get_restore_paths(paths, options=None):
    """Get Restore Paths

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
    return [
        os.path.relpath(
            path,
            user_config_manager.get_property('bin_path')
        ) for path in deleting_list
    ]
