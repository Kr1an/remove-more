from utils.commands import delete_command, restore_command


def execute_command(paths, options):
    if 'remove' in options['mods']:
        return delete_command.delete(paths, options)

    if 'restore' in options['mods']:
        return restore_command.restore(paths, options)
