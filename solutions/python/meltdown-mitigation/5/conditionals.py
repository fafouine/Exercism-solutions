def is_criticality_balanced(temperature, neutrons_emitted):
    """Determine if the reactor is balanced in criticality.

    Parameters:
        - temperature (int or float): The temperature value in kelvin.
        - neutrons_emitted (int or float): The number of neutrons emitted per second.

    Returns:
        bool: Is the reactor balanced in criticality?

    Note: A reactor is balanced in criticality if it satisfies the following conditions:
        - The temperature is less than 800k.
        - The numbver of neutrons emitted per second is greater than 500.
        - The product of the temperature and the emitted neutrons per second is less than 500 000.
    """

    heat = temperature * neutrons_emitted
    return temperature < 800 and neutrons_emitted > 500 and heat < 5E5

def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess the reactor's efficiency.

    Parameters:
        - voltage (int or float): The voltage the reactor is operating at.
        - current (int or float): The current in Watts going through the reactor.
        - theoretical_max_power (int or float): The power level that corresponds to a 100% efficiency.

    Returns:
        - "green" if the efficiency is of 80% or more.
        - "orange" if the efficiency is of 60%  or more,
        - "red" if the efficiency is of 30% or more.
        - "black" if the efficiency is of less than 30%.
    """

    efficiency  = (voltage*current / theoretical_max_power) * 100
    
    if efficiency  >= 80:
        return "green"
    if efficiency >= 60:
        return "orange"
    if efficiency >= 30:
        return "red"
    return "black"


def fail_safe(temperature, neutrons_emitted, threshold):
    """Assess and return status code for the reactor.

    Parameters:
        temperature (int or float): The value of the temperature in kelvin.
        neutrons_produced_per_second (int or float): The neutron flux.
        threshold (int or float): The threshold for the category.

    Returns:
        - "LOW" if HEAT < 90 % of threshold.
        - "NORMAL" if HEAT +/- 10% of threshold
        - "DANGER" if HEAT is not in the above-stated ranges
    """
    
    heat = temperature * neutrons_emitted
    
    if heat <  0.9 * threshold:
        return "LOW"
    if 0.9 * threshold <= heat <= 1.1 * threshold:
        return "NORMAL"
    return "DANGER"