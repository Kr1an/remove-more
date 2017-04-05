"""Formatter

Module offers management capability of logging system.
To up and run, should first call setup(init function that setting up
default or custom logger depend on is there config file

"""
import logging
from utils.managers import app_config_manager
from utils.helpers.formatter import LvlDependFormatter


def setup(options=None):
    """Setup Function
    
    Init function for log_helper, should be called before logging
    anything
    
    Arguments:
        options: list of optional config params.
    Returns:
        value: 1/0 depend on success of operation.
        
    """
    try:
        if options is None:
            logging.root.disabled = True

        logging_config = app_config_manager.get_property('logger')

        fmt = LvlDependFormatter()
        hdlr = logging.StreamHandler()

        logger = logging.getLogger(logging_config['name'])
        logger.setLevel(logging.getLevelName(logging_config['level']))

        hdlr.setFormatter(fmt)
        logger.addHandler(hdlr)
        logger.setLevel(logging.DEBUG)

        if not options or 'silent' in options:
            logger.disabled = options['silent']

        return 0
    except Exception as e:
        logging.exception(e)
        return 1


def get_log():
    """Get Log Function

    Function allow getting particular logger

    Returns:
        value: custom of default logger.

    """
    try:

        return logging.getLogger(
            app_config_manager.get_property('logger.name')
        )
    except Exception as e:
        logging.exception(e)
        return logging

