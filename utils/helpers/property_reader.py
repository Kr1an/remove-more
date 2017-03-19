"""Property Reader.

Module is offer possibility to search in  python dict/json string by
property chaining: 'property1.property2.property3'.

Example:
    property_writer.set_property({
            "geometry" : {
                "northeast" : {
                    "lat" : 17.4677999,
                    "lng" : -83.06210009999999
                }
            }
        }, 'geometry.northeast.lat', '12', sep='.') returns '12'.

Does not use to find list element by index: returns 'None'.

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
        Returned Value: 'None' if property does not exist of
                parameters are not valid. Otherwise return
                'Value' if property does exist.

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
    except Exception as e:
        print(e)
        return None


def get_property_from_json(json_str, search_query, sep='.'):
    """Get Property From Json function

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
            Returned Value: 'None' if property does not exist of
                parameters are not valid. Otherwise return json
                representation of 'Value' if property does exist.

    """
    try:
        obj = json.loads(json_str)
        return get_property(obj, search_query, sep)
    except Exception as e:
        print(e)
        return None
