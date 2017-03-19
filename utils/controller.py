""" Controller Module.

This module is a controller to handle script
tasks with different command line arguments.
This is the main execution module.

"""
import argparse
import os


def main():
    arguments_parser = argparse.ArgumentParser()
    arguments_parser.add_argument(
        "-hw",
        "--hello_world",
        default=False,
        help="remove script",
        action="store_true"
    )

    arguments = arguments_parser.parse_args()

    if arguments.hello_world:
        print('hello world')
        print(os.getcwd())


if __name__ == "__main__":
    main()
