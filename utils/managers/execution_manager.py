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
from utils.commands import delete_command, restore_command, bin_command


def execute_command(paths=[], options=None):
    """Execute Command Function

    Execute commands in place after argument_manager.

    Args:
        paths: possible list of given paths to delete or restore. Do not use
            this argument to pass path to some location(ex. path to create bin)
        options: possible object with settings(mods) of needed command.

    """
    if 'remove' in options['mods']:
        return delete_command.delete(paths, options)

    if 'restore' in options['mods']:
        return restore_command.restore(paths, options)

    if 'empty_bin' in options['mods']:
        return bin_command.empty_bin(options)

    if 'create_bin' in options['mods']:
        return bin_command.create_bin(options['path'], options)

    if 'copy_bin' in options['mods']:
        return bin_command.copy_bin(options['path'], options)

    if 'move_bin' in options['mods']:
        return bin_command.move_bin(options['path'], options)

    if 'binpath' in options['mods']:
        return bin_command.get_bin_path(options)
