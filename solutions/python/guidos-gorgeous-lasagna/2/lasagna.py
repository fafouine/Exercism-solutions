"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2 # changed from 0 to reflect  the actual preparation time rather than simply initializing the constant

def bake_time_remaining(elapsed_bake_time):
    """Calcu1ate the bake time remaining.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the number of minutes the lasagna has been in the oven as an argument and returns how many minutes the lasagna still needs to bake based on the expected baking time.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calcu1ate the preparation time.
    Returns:
    int: The preparation time (in minutes) derived from number_of_layers.

    Function that takes the lasagna's number of layers as an argument and returns how many minutes it will take to prepare the lasagna based on the fact that each layer takes 2 minutes to prepare.
    """
    return PREPARATION_TIME * number_of_layers # changed from 2 * 'number_of_layers' to make code more reusable 
    # for other recipies
 
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total amount of time spent cooking.

    Returns:
        int: The total amount of time spent baking (in minutes) derived from 'preparation_time_in_minute' according to 'number_of_layers' and 'elapsed_bake_time'.

    Function that determines the preparation time of the lasagna by taking an argument 'number_of_layers' to use as an argument for the to 'preparation_time_in_minutes' function, adding the resulting number to the number of minutes spent baking the lasagna so far, and returns the result, which tells us how many minutes has been spent in the kitchen so far.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time