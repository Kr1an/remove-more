from utils.helpers import property_reader


config = {
    'name': {
        'short': 'rr',
        'normal': 'RemoveRestore'
    },
    'controller': {
        'relative_path_components': [
            '..',
            'controller.py'
        ]
    }
}


def get_property(search_query):
    return property_reader.get_property(config, search_query)
