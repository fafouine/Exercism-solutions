"""Functions for calculating steps in exchanging currency."""


def exchange_money(budget, exchange_rate):
    """Calculate the value held after applying the `exchange_rate` of the desirend curency to `budget`.

    Parameters:
        - budget (float): The amount of money you are planning to exchange.
        - exchange_rate(float): How much 1 USD represents in the chosen currency.

    Returns:
        float: The exchanged value of the USD into the forein currency
        """
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """Calculate currency left after an exchange.

    Parameters:
        - budget (float): The amount of money you own.
        - exchanging_value (float): The amount of your money you want to exchange now.

    Returns:
        float: the amount of change you will get.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """Calculate the total value of currency at current denomination.

    Parameters:
        - denomination (int): The value of a single unit (bill).
        - number_of_bills (int): The total number of units (bills).

    Returns:
        int: Calculated value of the units (bills).
    """
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """Calculate the number of currency units (bills) within the amount.

    Parameters:
        - amount (float): The total starting value.
        - denomination (int): The value of a single unit (bill).

    Returns:
        int: The number of units (bills) that can be obtained from the amount.
    """
    return amount // denomination


def get_leftover_of_bills(amount, denomination):
    """Calculate leftover amount after exchanging into bills.

    Parameters:
        - amount (float): The total starting value.
        - denomination (int): The value of a single unit (bill).

    Returns:
        float: The amount that is "leftover", given the current denomination.
    """
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calculate the maximum value of the new currency.

    Parameters:
        - budget (float): The amount of your money you are planning to exchange.
        - exchange_rate (float): The unit value of the foreign currency.
        - spread (int): The percentage that is taken as an exchange fee.
        - denomination (int) The value of a single unit (bill).

    Returns:
        int: The maximum value you can get in the new currency.
    """
    amount = budget / (exchange_rate * (1 + spread / 100))
    return  amount - get_leftover_of_bills(amount, denomination)
 