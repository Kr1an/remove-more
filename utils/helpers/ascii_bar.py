"""ASCII Bar Module

All module is all about getting progress bar string that could be than
used in different situation.

"""

# Constant shows how long progress bar is.
NUM_OF_ELEMENTS = 20


def get_progress_bar(value, max_value):
    """ Get Progress Bar Function
    
    Function generates ascii symbols progress bar with custom progress
    position and custom Length of bar.
    
    Arguments:
        value: absolute progress value.
        max_value: max absolute progress value.
    
    Return:
        value: string that represents progress bar with passed params.
    
    """

    done = int(float(value)/max_value * NUM_OF_ELEMENTS)
    more = NUM_OF_ELEMENTS - done
    percentage = int(float(done)/(more+done) * 100)
    return '{}{} {}%'.format(
        '*' * done,
        ' ' * more,
        percentage
    )
