"""Functions for calculating steps in exchanging currency.
"""


def exchange_money(budget, exchange_rate):
    """Calculate estimated value after exchange.

    Parameters:
       budget (float): The amount of money you are planning to exchange.
       exchange_rate (float): The unit value of the foreign currency.

    Returns:
        float: The exchanged value of the foreign currency you can receive.
    """
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """Calculate currency left after an exchange.
ÿ
    Parameters:
        budget (float): The amount of money you own.
        exchanging_value (float): The amount of your money you want to exchange now.

    Returns:
        float: Then̈  amount left of your starting currency after the exchange
    """
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """Calculate the total value of currency at current denomination.

    Parameters:
        denomination (int): The value of a single unit (bill).
        number_of_bills (int): The total number of units (bills).

    Returns:
        int: Calculated value of the units (bills).k
    """
    return int(denomination * number_of_bills)


def get_number_of_bills(amount, denomination):
    """Calculate the number bills that will be received according to the given amount.

    Parameters:
        amount (float): The total starting value.
        denomination (int): The value of a single bill.

    Returns:
        int: The number of bills that can be obtained from the amount.
    """
    return amount // denomination
    

def get_leftover_of_bills(amount, denomination):
    """Calculate leftover amount after exchanging into bills.

    Parameters:
        amount (float): The total starting value.
        denomination (int): The value of a single unit (bill).

    Returns:
        float: The amount that is "leftover", given the current denomination.
    """
    return round(amount % denomination, 2)


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calculate the maximum value of the new currency.

    Parameters:
    - budget (float): The amount of money to exchange.
    - exchange_rate (float): The unit value of the foreign currency.
        spread (int): The percentage that is taken as an exchange fee.
        denomination (int) The value of a single bill. 

 Returns:
        int: The maximum value you can get in the new currency.
        """
    amount = exchange_money(budget, exchange_rate * (1 + spread / 100))

    number_of_bills = get_number_of_bills(amount, denomination)

    return int(get_value_of_bills(denomination, number_of_bills))
    
