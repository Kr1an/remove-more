import os

from utils.managers import config_manager


def is_installed():
    """Check script existing"""
    try:
        with open(os.path.expanduser('~' + os.sep + '.bashrc')) as f:
            script = 'alias {}'.format(
                config_manager.get_property('name.short')
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
                config_manager.get_property('name.short')
            )
            for line in lines:
                if script not in line:
                    f.write(line)
    except Exception as e:
        print(e)


def install():
    """Install script to .bashrc"""

    os.system(get_install_script())


def get_install_script():
    """Generate bash command to install script"""

    return 'echo alias {}=\\\"{}\\\" >> ~/.bashrc'.format(
        config_manager.get_property('name.short'),
        'python {}'.format(
            os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__),
                    *config_manager.get_property(
                        'controller.relative_path_components'
                    )
                )
            )
        )
    )

