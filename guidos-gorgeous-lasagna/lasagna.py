"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_MINUTES_PER_LAYER = 2


def bake_time_remaining(bake_time_elapsed):
    """Calculate the bake time remaining.

    :param bake_time_elapsed: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - bake_time_elapsed


def preparation_time_in_minutes(num_layers):
    """Calculate the prep time. In minutes.

    :param num_layers: int
    :return: int - prep time for number of layers provided
    """
    return num_layers * PREPARATION_MINUTES_PER_LAYER


def elapsed_time_in_minutes(num_layers, already_elapsed):
    """Calculate how much time a lasagna has been baking and being prepared, given
    the number of layers and time that has elapsed in the oven. Do I feel a bit
    sheepish writing this? I do.

    :param num_layers: int
    :param already_elapsed: int
    :return: int
    """
    return preparation_time_in_minutes(num_layers) + already_elapsed
