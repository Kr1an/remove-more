import argparse

from utils.managers import installmaster, oscheckmanager, testmaster


# Used modules:
#
#     oscheckmanager -- manager, should provide next functions:
#         is_supported_platform -- is current platform supported
#
#     installmaster -- manager, should provide next functions:
#         remove -- remove script
#         install -- install script
#         is_installed -- check if the script is already installed


def remove():
    """Remove function.

    Run installmaster(manger of install/remove commands) remove method to
    reinstall(remove) script from memory.

    """
    if installmaster.is_installed():
        installmaster.remove()


def install():
    """Install function.

    Run installmaster(manger of install/remove commands) install method to
    install(bind) script to memory.

    """
    if not installmaster.is_installed():
        installmaster.install()


def test():
    """Start test function

    Run test case command in testmaster(manager)
    that search for unittest class cases.

    """
    testmaster.run_tests()


def setup():
    """Setup function.

    Function checked cmd-line(terminal) args. Run needed function according
    to args:
        --remove(default: False): execute remove script. Short name -r.
        --test(default:False): execute test script. Short name -t. Needed
            for development
        default: execute install script.

    """
    if oscheckmanager.is_supported_platform():
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

        if arguments.remove:
            remove()

        if not arguments.remove:
            install()

if __name__ == "__main__":
    # Start point for cmd execution
    setup()
