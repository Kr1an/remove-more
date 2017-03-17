import sys

from utils.managers import app_config_manager


def is_supported_platform():
    """Function check if platform is supported"""
    platform_name = sys.platform.lower()
    return platform_name in app_config_manager.get_property(
        'supported_platforms'
    )
