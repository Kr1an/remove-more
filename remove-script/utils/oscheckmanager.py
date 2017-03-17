import sys
from utils import configmanager


def is_supported_platform():
    platform_name = sys.platform.lower()
    return platform_name in configmanager.get_property('supported_platforms')
