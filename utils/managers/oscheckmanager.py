import sys

from utils.managers import configmanager


def is_supported_platform():
    """Function check if platform is supported"""
    platform_name = sys.platform.lower()
    return platform_name in configmanager.get_property('supported_platforms')
