import logging
from utils.managers import app_config_manager
from utils.helpers.formatter import LvlDependFormatter


def setup(options=None):
    try:
        logging_config = app_config_manager.get_property('logger')

        fmt = LvlDependFormatter()
        hdlr = logging.StreamHandler()




        logger = logging.getLogger(logging_config['name'])
        logger.setLevel(logging.getLevelName(logging_config['level']))

        hdlr.setFormatter(fmt)
        logger.addHandler(hdlr)
        logger.setLevel(logging.DEBUG)

        if 'silent' in options:
            logger.disabled = options['silent']

        return 0
    except Exception as e:
        if 'silent' in options:
            logger.disabled = True
        logging.exception(e)
        return 1


def get_log():
    try:
        return logging.getLogger(
            app_config_manager.get_property('logger.name')
        )
    except Exception as e:
        logging.exception(e)
        return logging

