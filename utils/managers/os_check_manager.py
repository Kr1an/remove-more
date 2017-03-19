"""Os Check Manager.

Module is needed to check if platform is supported.

Example:
    os_check_manager.is_supported_platform()

Module is not finished and could be changed.

"""
import sys

from utils.managers import app_config_manager


def is_supported_platform():
    """Is Supported Platform Function.

    Function check if platform is supported

    Returns:
        Boolean shows is platform supported.

    """
    platform_name = sys.platform.lower()
    supported_platforms = app_config_manager.get_property('supported_platforms')
    return platform_name in supported_platforms
