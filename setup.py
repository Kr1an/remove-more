import argparse
import os

from utils.managers import install_master, os_check_manager, test_master


#
# Used modules:
#
#     oscheckmanager: manager, should provide next functions:
#         is_supported_platform: is current platform supported
#
#     installmaster: manager, should provide next functions:
#         remove: remove script
#         install: install script
#         is_installed: check if the script is already installed
#


def remove():
    """Remove function.

    Run installmaster(manger of install/remove commands) remove method to
    reinstall(remove) script from memory.

    """
    if install_master.is_installed():
        install_master.remove()


def install():
    """Install function.

    Run installmaster(manger of install/remove commands) install method to
    install(bind) script to memory.

    """
    if not install_master.is_installed():
        install_master.install(
            {
                'app_location': os.path.dirname(os.path.abspath(__file__))
            }
        )


def test():
    """Start test function

    Run test case command in testmaster(manager)
    that search for unittest class cases.

    """
    test_master.run_tests()


def setup():
    """Setup function.

    Function checked cmd-line(terminal) args. Run needed function according
    to args:
        --remove(default: False): execute remove script. Short name -r.
        --test(default:False): execute test script. Short name -t. Needed
            for development
        default: execute install script.

    """
    if os_check_manager.is_supported_platform():
        arguments_parser = argparse.ArgumentParser()
        arguments_parser.add_argument(
            "-r",
            "--remove",
            default=False,
            help="remove script",
            action="store_true"
        )
        arguments_parser.add_argument(
            "-t",
            "--test",
            default=False,
            help="run test scripts",
            action="store_true"
        )
        arguments = arguments_parser.parse_args()

        if arguments.test:
            test()
        elif arguments.remove:
            remove()
        elif not arguments.remove:
            install()

if __name__ == "__main__":
    # Start point for cmd execution
    setup()
