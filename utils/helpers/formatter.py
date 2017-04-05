import logging
import sys

from utils.managers import app_config_manager

class LvlDependFormatter(logging.Formatter):
    def __init__(self, fmt="%(levelno)s: %(msg)s"):
        logging.Formatter.__init__(self, fmt)


    def format(self, record):
        format_orig = self._fmt
        formats = app_config_manager.get_property('logger.formats')
        print(logging.getLevelName(record.levelno))
        print(formats)
        print(logging.getLevelName(record.levelno) in formats)

        if logging.getLevelName(record.levelno) in formats:
            self._fmt = formats[logging.getLevelName(record.levelno)]
            print(self._fmt)
        else:
            self._fmt = formats['default']

        result = logging.Formatter.format(self, record)

        self._fmt = format_orig

        return result