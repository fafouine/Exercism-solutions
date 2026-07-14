"""Determine if a given year is a leap year or not."""


def leap_year(year):
    """Is this a leap year?"""
    return (not year % 4 and 
            (not year % 400 or not not year % 100)
           )