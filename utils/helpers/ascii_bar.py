NUM_OF_ELEMENTS = 20


def get_progress_bar(value, range):
    done = int(float(value)/range * NUM_OF_ELEMENTS)
    more = NUM_OF_ELEMENTS - done
    percentage = int(float(done)/(more+done) * 100)
    return '{}{} {}%'.format(
        '*' * done,
        ' ' * more,
        percentage
    )
