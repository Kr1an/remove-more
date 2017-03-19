import os

from utils.managers import user_config_manager, app_config_manager
from utils.helpers.property_reader import *


def is_installed():
    """Check script existing"""
    try:
        with open(os.path.expanduser('~' + os.sep + '.bashrc')) as f:
            script = 'alias {}'.format(
                user_config_manager.get_property('name.short')
            )
            check_lines = (line.startswith(script) for line in f)
            return any(check_lines)
    except Exception as e:
        print(e)


def remove():
    """Remove script from .bashrc"""
    try:
        with open(os.path.expanduser('~' + os.sep + '.bashrc'), 'r') as f:
            lines = f.readlines()
    except Exception as e:
        print(e)

    try:
        with open(os.path.expanduser('~' + os.sep + '.bashrc'), 'w') as f:
            script = 'alias {}'.format(
                user_config_manager.get_property('name.short')
            )
            for line in lines:
                if script not in line:
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
    """Generate bash command to install script"""

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

    Initialize app_config, config, config_default

    """

    app_config_manager.initialize()
    user_config_manager.initialize()
    app_config_manager.set_property('user_config.use_custom', True)
    user_config_manager.initialize()
