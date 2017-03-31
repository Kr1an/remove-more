""" Install Master Module.

Module offers all management functionality
with removing, installing, checking of project script.

Example:
    install_master.is_installed()

Uses user_config_manager, app_config_manager
as a base of it's functionality.

"""
import os

from utils.managers import user_config_manager, app_config_manager
from utils.managers import bin_config_manager


def is_installed():
    """Is Installed Function.

    Check script existing by reading ~/.bashrc
    file and finding script line there.

    """
    try:
        with open(os.path.expanduser('~' + os.sep + '.bashrc')) as f:
            part_of_script = '/remove-more/utils/controller.py'
            check_lines = (part_of_script in line for line in f)
            return any(check_lines)
    except Exception as e:
        print(e)


def remove():
    """Remove Function

    Remove script from .bashrc.

    """
    try:
        with open(os.path.expanduser('~' + os.sep + '.bashrc'), 'r') as f:
            lines = f.readlines()
    except Exception as e:
        print(e)

    try:
        with open(os.path.expanduser('~' + os.sep + '.bashrc'), 'w') as f:
            part_of_script = '/remove-more/utils/controller.py'
            for line in lines:
                if part_of_script not in line:
                    f.write(line)
    except Exception as e:
        print(e)


def install(install_config={}):
    """Install Function

    Installing script to bash. Setting up app_config properties

    Args:
        install_config: dict of extra installing params:
            'app_base_dir': '<path ot app base directory>'

    """

    os.system(get_install_script())


def get_install_script():
    """Get Install Script Function.

    Generate bash command to install script

    Returns:
        Install script code body(type == str)

    """
    return 'echo alias {}=\\\"{}\\\" >> ~/.bashrc'.format(
        user_config_manager.get_property('name.short'),
        'python {}'.format(
            os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__),
                    *[
                        '..',
                        'controller.py'
                    ]
                )
            )
        )
    )


def init_config_files(init_config={}):
    """Initialize Function

    Initialize app_config_manager, user_config_manager.

    Attributes:
        init_config is dict with init configuration options.
        It's not necessary attribute.

    """

    app_config_manager.initialize()
    user_config_manager.initialize()
    app_config_manager.set_property('user_config.use_custom', True)
    user_config_manager.initialize()
    bin_config_manager.initialize()
