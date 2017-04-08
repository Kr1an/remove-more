""" Controller Module.

This module is a controller to handle script
tasks with different command line arguments.
This is the main execution module.

"""
from utils.managers import argument_manager, execution_manager
from utils.helpers import log_helper
from utils.managers import user_config_manager


def main():
    """Main Controller function

    It's start point for script execution.
    Handles all command line arguments and run other functionality according
    to arguments

    """

    [paths, options] = argument_manager.parse_arguments()
    log_helper.setup(options)
    user_config_manager.setup(options)
    return execution_manager.execute_command(paths, options)


if __name__ == "__main__":
    main()

