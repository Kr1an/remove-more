"""Package to search in obj, json for properties

Package is needed to search such query: 'property1.property2.property3'
with in json or python dictionary.

Does not use to find list element by index: returns 'None'

"""

import json
import copy


def set_property(obj, search_query, value, sep='.'):
    """Set Property function

    Function's needed to find properties with search query and replace this
    property with 'value'.

    Args:
        obj:
            Object in which, needed to be changed.
            Example: {'name': 'some_name', 'age': 'some_age'}.
        search_query:
            Chain of property that needed to be find as a string separated
            by sep(default: '.').
            Example: property1.property2.property3...
        value:
            Value that needed to be replaced.
        sep:
            Character, that separate properties in property chain.
            Default: '.'(point)

    Returns:
        Returned Value: 'None' if property does not exists or parameters
            are not valid or value is not valid. 'Value' of dict type if
            function finished with success.

    """

    try:
        if value is None or search_query is None:
            return None
        obj_to_change = copy.deepcopy(obj)
        container = obj_to_change
        targets = search_query.split(sep)[:-1]
        property_to_change = search_query.split(sep)[-1]

        for target in targets:
            if isinstance(container, dict) and target in container:
                container = container[target]
            else:
                return None
        if isinstance(container, dict) and property_to_change in container:
            container[property_to_change] = value
            return obj_to_change
        else:
            return None
    except:
        return None


def set_property_from_json(json_str, search_query, value, sep='.'):
    """Get Property function

    Function's needed to find properties with search query and replace this
    property with 'value'.

    Args:
        json_str:
            Json representation of object which needed to be changed.
            Example: {'name': 'some_name', 'age': 'some_age'}.
        search_query:
            Chain of property that needed to be find as a string separated
            by sep(default: '.').
            Example: property1.property2.property3...
        value:
            Value that needed to be replaced.
        sep:
            Character, that separate properties in property chain.
            Default: '.'(point)

    Returns:
        Returned Value: 'None' if property does not exists or parameters
            are not valid or value is not valid. json representation of
            'Value' type if function finished with success.

    """
    try:

        obj = json.loads(json_str)
        result = set_property(obj, search_query, value, sep)

        return json.dumps(result) if result is not None else None
    except:
        return None
