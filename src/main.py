"""
random number generator
Author: Charles Spencer
"""

from random import randint


def num_str(top: str) -> str:
    """Return a string with a die roll."""
    if top.isnumeric():
        return f"Your number is {randint(1, int(top))}."
    else:
        return "Please enter a number."
