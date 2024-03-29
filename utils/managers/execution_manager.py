"""Execution Manager Module.

Module uses commands module to execute user commands.
Only accessible for outer scope function is 'execute_command', to which,
You need to pass options, that describe which command it's needed to execute.

Possible commands:
* remove
* restore

Conversation with params:
* if command is about restore/delete some files, than function should
get 2 arguments: first one is a list of paths of regex path, second is option
object with nessesary property mods(typeof list) that describe what manager
should execute.
* If path argument shows needed destination of location, this location should
 be within 'path' property of 'options' object, but not in paths arguments.

Example:
    execute_command({'mods': ['restore', 'with_no_bin', ...]})

Module is under construction. Could be extended.

"""
import os

from utils.commands import delete_command, restore_command, bin_command
from utils.managers import app_config_manager, user_config_manager
from utils.managers import bin_config_manager

from setting.DEFAULT_CONFIGS import ERROR_MESSAGES


def execute_command(paths=[], options=None):
    """Execute Command Function

    Execute commands in place after argument_manager.

    Args:
        paths: possible list of given paths to delete or restore. Do not use
            this argument to pass path to some location(ex. path to create bin)
        options: possible object with settings(mods) of needed command.
    
    Remark:
        To run empty_bin command could be used 
            both 'binempty' or 'empty_bin' key words.
        To run move_bin command could be used 
            both 'binmove' or 'move_bin' key words.
        To run 'create_bin' command could be used
            both 'bincreate' or 'create_bin' key words.
        
    """
    if not _valid_command(paths, options):
        return 1

    if 'remove' in options['mods']:
        return delete_command.delete(paths, options)

    if 'restore' in options['mods']:
        return restore_command.restore(paths, options)

    if 'binempty' in options['mods'] or 'empty_bin' in options['mods']:
        return bin_command.empty_bin(options)

    if 'bincreate' in options['mods'] or 'create_bin' in options['mods']:
        return bin_command.create_bin(options['path'], options)

    if 'bincopy' in options['mods'] or 'copy_bin' in options['mods']:
        return bin_command.copy_bin(options['path'], options)

    if 'binmove' in options['mods'] or 'move_bin' in options['mods']:
        return bin_command.move_bin(options['path'], options)

    if 'binpath' in options['mods']:
        return bin_command.get_bin_path(options)

    if 'binprint' in options['mods']:
        return bin_command.print_bin(options)


def _valid_command(paths, options):
    try:
        if not app_config_manager.is_valid():
            raise Exception(ERROR_MESSAGES['app_config_error'])
        elif not user_config_manager.is_valid():
            raise Exception(ERROR_MESSAGES['user_config_error'])
        elif not bin_config_manager.is_valid():
            raise Exception(ERROR_MESSAGES['bin_config_error'])
        elif not os.path.isdir(user_config_manager.get_property('bin_path')):
            if 'bincreate' not in options['mods']:
                raise Exception(ERROR_MESSAGES['bin_not_exists'])
        return True
    except Exception as e:
        print(e)
        return False
