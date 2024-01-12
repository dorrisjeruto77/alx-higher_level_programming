#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Add two numbers, which are either integers or floats.

    Args:
        a (int/float): The first number.
        b (int/float, optional): The second number. Defaults to 98.

    Returns:
        int: The sum of a and b, converted to an integer.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    return int(a) + int(b)
