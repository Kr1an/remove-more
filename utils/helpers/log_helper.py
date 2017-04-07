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
        # If it's 'silent' mod or options was not passed than
        # disable logger, because it's either test mod or lib kind usage
        # of script
        if options is None or 'silent' in options:
            logging.root.disabled = True
            return 0

        logging_config = app_config_manager.get_property('logger')

        formatter = LvlDependFormatter()
        handler = logging.StreamHandler()

        logger = logging.getLogger(logging_config['name'])

        # Try to find loglvl option in params and if exists,
        # try to equal it to logger log level.
        if 'loglvl' in options and options['loglvl'] in logging._levelNames:
            logger.setLevel(logging.getLevelName(options['loglvl']))
        # Otherwise get loglevel from config file.
        else:
            logger.setLevel(logging.getLevelName(logging_config['level']))

        # Set up logger is formatter and empty handlers.
        handler.setFormatter(formatter)
        logger.handlers = []
        logger.addHandler(handler)

        # Make logger disabled if silent mod
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
        # Trying to get needed logger
        logger = logging.getLogger(
            app_config_manager.get_property('logger.name')
        )
        logging.root.handlers = []
        handler = logging.StreamHandler()
        logging.root.addHandler(handler)
        logging.root.setLevel(logging.CRITICAL)

        # if try was successful return logger
        if len(logger.handlers):
            logging.root.handlers = []
            return logger
        # Otherwise return default logging.root logger
        else:
            return logging.root
    except Exception as e:
        return logging.root

