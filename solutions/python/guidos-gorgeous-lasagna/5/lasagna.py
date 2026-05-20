"""Determine how long cooking Guido's Gorgeous Lasagna will take to be done."""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def  bake_time_remaining(elapsed_bake_time):  
    """Calculate the remaining bake time in minutes.

    Arguments: 
        - 'elapsed_bake_time' (int):
            actual minutes the lasagna has been in the oven.

    Returns:
        -  (int): the remaining bake time (in minutes).
        
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate  the total preparation time.

    Arguments:
        - 'number_of_layers' (int):
            number of layers to be added to the lasagna.

    Returns:
        -(int):  total preparation time in minutes.
    
    """
    return number_of_layers * PREPARATION_TIME


def  elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total amount of time spent

    Arguments:
        - 'number_of_layers' (int):
            number of layers that were added to the lasagna.
        - 'elapsed_bake_time' (int):
            amount of minutes the lasagna has been baking.

    Returns: 
        - (int): total elapsed time (prep time + bake time) in minutes.
    
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    