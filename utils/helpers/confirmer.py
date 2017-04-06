"""Confirmer Module.

Custom module that allow to question user within terminal question and
get answer as True/False value.
Module is not extendable for other input output stream but terminal input
stream and terminal output stream.

"""
import sys
import logging

from utils.managers import app_config_manager


def confirm_question(question, default="yes", options=None):
    """Ask a yes/no question via raw_input() and return their answer.
    
    Arguments:
        question: is a string that is presented to the user.
        default: is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).
        options: list of options
    
    Returns:
        value: boolean True for 'yes' answer, False --'no'.

    """
    if not options or 'confirm' not in options:
        return True
    logger = logging.getLogger(app_config_manager.get_property('logger.name'))
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        logger.info(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            logger.info(
                "Please respond with 'yes' or 'no' (or 'y' or 'n').\n")
