"""Determine if a given year is a leap year or not."""

def leap_year(year):
    divisible_by_four, divisible_by_hundred, divisible_by_four_hundred = year % 4 == 0, year % 100 == 0, year % 400 == 0
    return divisible_by_four and (divisible_by_four_hundred or not divisible_by_hundred)