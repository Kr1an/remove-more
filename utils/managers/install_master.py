import os

from utils.managers import config_manager


def is_installed():
    """Check script existing"""
    try:
        with open(os.path.expanduser('~' + os.sep + '.bashrc')) as f:
            script = 'alias {}'.format(
                config_manager.get_property('short_script_name')
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
                config_manager.get_property('short_script_name')
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
    path_components = config_manager.get_property('script_path_from_base')
    path_base = os.path.dirname(os.path.abspath(__file__))
    script = 'python {}'.format(path_base + os.sep + path_components[1])

    return 'echo alias {}=\\\"{}\\\" >> ~/.bashrc'.format(
        config_manager.get_property('short_script_name'),
        script
    )

