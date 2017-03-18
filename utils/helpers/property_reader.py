"""Package to search in obj, json for properties

Package is needed to search such query: 'property1.property2.property3'
with in json or python dictionary.

Does not use to find list element by index: returns 'None'

"""

import json


def get_property(obj, search_query, sep='.'):
    """Get Property function

    Function's needed to find properties with search query.

    Args:
        obj:
            Object in which, needed property lays.
            Example: {'name': 'some_name', 'age': 'some_age'}.
        search_query:
            Chain of property that needed to be find as a string separated
            by sep(default: '.').
            Example: property1.property2.property3...
        sep:
            Character, that separate properties in property chain.
            Default: '.'(point)

    Returns:
        None: returns 'None' if property does not exists.
            returns 'None' if parameters are not valid.
        Value: returns 'Value' if property does exists.

    """

    try:
        container = obj
        targets = search_query.split(sep)

        for target in targets:
            if isinstance(container, dict) and target in container:
                container = container[target]
            else:
                return None

        return container
    except:
        return None


def get_property_from_json(json_str, search_query, sep='.'):
    """Get Property function

        Function's needed to find properties
        with search query within json.

        Args:
            json_str:
                JSON obj in which, needed property lays.
                Example: '{"name": "some_name", "age": "some_age"}'.
            search_query:
                Chain of property that needed to be find as a string separated
                by sep(default: '.').
                Example: 'property1.property2.property3'
            sep:
                Character, that separate properties in property chain.
                Default: '.'(point)

        Returns:
            None: returns 'None' if property does not exists.
                returns 'None' if parameters are not valid.
            Value: returns 'Value' if property does exists.

    """
    try:
        obj = json.loads(json_str)
        return get_property(obj, search_query, sep)
    except:
        return None
