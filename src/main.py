"""
random number generator
Author: Charles Spencer
"""

from random import randint


def num_str(top: int) -> str:
    """Return a string indicating whether num is odd or even."""
    if top.isnumeric():
        return f"Your number is {randint(1, int(top))}."
    else:
        return "Please enter a number."
