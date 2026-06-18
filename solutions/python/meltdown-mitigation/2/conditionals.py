"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify if the reactor's criticality is balanced.

    Parameters:
        - temperature (int or float): The temperature value in kelvin.
        - neutrons_emitted (int or float): The number of neutrons emitted per second.

    Returns:
        bool: Is criticality balanced?
    """
    if temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500000:
        return True
    else:
        return False


def efficiency_percentage(voltage, current, theoretical_max_power):
    """Determine at what percentage of capacity the reactor is running.

    Parameters:
        - voltage (int or float): Voltage value.
        - current (int or float): Current value.
        - theoretical_max_power (int or float): The power level that corresponds to 100% efficiency.

    Returns:
        int: How efficiently is the reactor running out of 100.
    """
    return ((voltage * current) / theoretical_max_power) * 100 

    
def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    Parameters:
        - voltage (int or float): Voltage value.
        - current (int or float): Current value.
        - theoretical_max_power (int or float): The power level that corresponds to 100% efficiency.

    Returns:
        str: One of ('green', 'orange', 'red', or 'black').

    Note:
        Efficiency can be grouped into 4 bands:
            1. green -> efficiency of 80% or more,
            2. orange -> efficiency of less than 80% but at least 60%,
            3. red -> efficiency below 60%, but still 30% or more,
            4. black ->  less than 30% efficient.

        The percentage value is calculated as
        (generated power/ theoretical max power)*100
        where generated power = voltage * current
    """
    if efficiency_percentage(voltage, current, theoretical_max_power) >= 80:
        return "green"
    elif 80 > efficiency_percentage(voltage, current, theoretical_max_power) >= 60:
        return "orange"
    elif 60 > efficiency_percentage(voltage, current, theoretical_max_power) >= 30:
        return "red"
    else:
        return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    Parameters:
        temperature (int or float): The value of the temperature in kelvin.
        neutrons_produced_per_second (int or float): The neutron flux.
        threshold (int or float): The threshold for the category.

    Returns:
        str: One of ('LOW', 'NORMAL', 'DANGER').

    Note:
        1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
        2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
        3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """
    if temperature * neutrons_produced_per_second < (threshold * 90) / 100:
        return "LOW"
    elif (threshold * 110) / 100 >= temperature * neutrons_produced_per_second >= (threshold * 90) / 100:
        return "NORMAL"
    else:
        return "DANGER"
