"""Formatter

Module offers custom formatter with next politics: change format depend on
logging level.

"""
import logging
import sys

from utils.managers import app_config_manager


class LvlDependFormatter(logging.Formatter):
    """Custom Formatter Class
     
     Class choose needed format of logging messages depend
     on level name. Should be used with log_helper module
    
    """
    def __init__(self, fmt="%(levelno)s: %(msg)s"):
        logging.Formatter.__init__(self, fmt)

    def format(self, record):
        """Format Method.
        
        Returns right format depend on level logging name
        
        """
        format_orig = self._fmt

        # Get custom formatter config
        formats = app_config_manager.get_property('logger.formats')

        # Choose needed formatter depend on logging level.
        # If level does not exists, choose default formatter.
        if logging.getLevelName(record.levelno) in formats:
            self._fmt = formats[logging.getLevelName(record.levelno)]
        else:
            self._fmt = formats['default']

        result = logging.Formatter.format(self, record)
        self._fmt = format_orig
        return result