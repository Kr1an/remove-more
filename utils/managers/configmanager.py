config = {

    #
    # Not used part
    #

    'name': {
        'short': 'rr',
        'normal': 'RemoveRestore'
    },
    'controller': {
        'name': 'controller.py'
    },

    #
    # Duplicated json obj
    #

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
    ],

}


def get_property(search_query):

    # search_result = config
    # search_components = search_query.split('.')

    if search_query in config:
        return config[search_query]
    else:
        return None


