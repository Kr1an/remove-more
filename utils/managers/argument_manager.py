import argparse


def parse_arguments():
    arguments_parser = argparse.ArgumentParser()
    add_optional_arguments(arguments_parser)
    add_positional_arguments(arguments_parser)
    arguments = arguments_parser.parse_args()
    return [get_paths(arguments), get_options(arguments)]


def get_paths(arguments):
    return arguments.paths


def get_options(arguments):
    # Some staff to get different options goes here
    mock = {
        'mods': [
            'remove',
            'with_no_bin'
        ],
        "prop1": True,
        "prop2": 42,
        'prop3': 'hello, world'

    }
    options = _generate_options()
    return options or mock


def add_optional_arguments(arguments_parser):
    arguments_parser.add_argument(
        "-hw",
        "--hello_world",
        default=False,
        help="remove script",
        action="store_true"
    )


def add_positional_arguments(arguments_parser):
    arguments_parser.add_argument('paths', type=str, nargs='*')


def _generate_options():
    return None
