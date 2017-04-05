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
        if options is None or 'silent' in options:
            logging.root.disabled = True
            return 0

        logging_config = app_config_manager.get_property('logger')

        formatter = LvlDependFormatter()
        handler = logging.StreamHandler()

        logger = logging.getLogger(logging_config['name'])
        logger.setLevel(logging.getLevelName(logging_config['level']))

        handler.setFormatter(formatter)
        logger.handlers = []
        logger.addHandler(handler)
        if options is None or 'silent' in options:
            logger.disabled = True
            return 0

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

        logger = logging.getLogger(
            app_config_manager.get_property('logger.name')
        )
        logging.root.handlers = []
        handler = logging.StreamHandler()
        handler1 = logging.StreamHandler()
        logging.root.addHandler(handler)
        logging.root.addHandler(handler1)
        logging.root.setLevel(logging.CRITICAL)
        if len(logger.handlers):
            logging.root.handlers = []
            return logger
        else:
            return logging.root
    except Exception as e:
        return logging.root

