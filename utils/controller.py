import argparse
import sys
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
