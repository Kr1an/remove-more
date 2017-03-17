
config = {
    'short_script_name': 'rr',
    'script_name': 'RemoveRestore',
    'supported_platforms': [
        'linux',
        'linux2'
    ],
    'version': '0.0.1',
    'script_path_from_base': [
        'utils',
        'controller.py'
    ]
}


def get_property(name):
    if name in config:
        return config[name]
    else:
        return None
