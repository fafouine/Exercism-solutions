def leap_year(year):
    """Determine if a given year is a leap year or not."""
    divisable_by_four, divisable_by_hundred, divisable_by_four_hundred = year % 4 == 0, year % 100 == 0, year % 400 == 0
    condition_1 = divisable_by_four and not divisable_by_hundred
    condition_2 = divisable_by_four and (divisable_by_hundred and divisable_by_four_hundred)

    return condition_1 or condition_2

