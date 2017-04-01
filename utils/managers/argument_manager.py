import argparse

from setting.DEFAULT_CONFIGS import ARGS_CONFIG


def parse_arguments():
    arguments_parser = argparse.ArgumentParser()
    add_optional_arguments(arguments_parser)
    add_positional_arguments(arguments_parser)
    arguments = arguments_parser.parse_args()
    return [arguments.paths, _get_options(arguments)]


def _get_options(arguments):
    options = {'mods':[]}
    conditions = [
        (arguments.binmove, ['binmove']),
        (arguments.bincopy, ['bincopy']),
        (arguments.bincreate, ['bincreate']),
        (arguments.binempty, ['binempty']),
        (arguments.restore, ['restore']),
        (not arguments.restore, ['remove'])
    ]

    for condition in conditions:
        if condition[0]:
            if type(condition[0])!=bool:
                options.update({'path': condition[0]})
            options['mods'] += condition[1]
            break

    return options

def add_optional_arguments(arguments_parser):
    for argument in ARGS_CONFIG:
        arguments_parser.add_argument(
            argument['shortcut'],
            argument['name'],
            action=argument['action'],
            help=argument['help']
        )

def add_positional_arguments(arguments_parser):
    arguments_parser.add_argument('paths', type=str, nargs='*')

