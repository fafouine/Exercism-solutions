EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def  bake_time_remaining(elapsed_bake_time):
    # improved docstring
    """\
    Calculates the remaining bake time in minutes.

    Arguments: 
        - 'elapsed_bake_time' (int):
            actual minutes the lasagna has been in the oven.

    Returns:
        -  (int): the remaining bake time (in minutes).
    
    Calculates the remaining bake time by substracting 
    the elapsed time from the expected bake time.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """\
    Calculates  the total preparation time.

    Arguments:
        - 'number_of_layers' (int):
            number of layers to be added to the lasagna.

    Returns:
        -(int):  total preparation time in minutes.

    Calculates the preparation time by multiplying  the 
    number of layers by each of their preparation times
    """
    return number_of_layers * PREPARATION_TIME


def  elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """\
    Calculate the total amount of time spent

    Arguments:
        - 'number_of_layers' (int):
            number of layers that were added to the lasagna
        - 'elapsed_bake_time' (int):
            amount of minutes the lasagna has been baking

    Returns: 
        - (int): total elapsed time (prep time + bake time) in minutes

    Calculates  the total elapsed time by utilizing the 
    'preparation_time_in_minutes(number_of_layers)' function
    to add the prep time to the baking time. 
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    