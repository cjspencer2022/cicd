"""
random number generator
Author: Charles Spencer
"""

from random import randint


def num_str(top: str) -> str:
    """Return a string with a die roll."""
    try:
        top = int(top)
        return f"Your number is {randint(1, top)}."
    except ValueError:
        return "Please enter a whole number."
