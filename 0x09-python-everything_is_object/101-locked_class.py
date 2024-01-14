#!/usr/bin/python3

"""
Module documentation: LockedClass module.
This module provides the LockedClass class which restricts attribute creation.
"""


class LockedClass:
    """
    A class that only allows creating an attribute named 'first_name'.
    Attempts to set or access other attributes result in an AttributeError.
    """

    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")

    def __getattr__(self, name):
        raise AttributeError(f"'LockedClass' object has no attribute '{name}'")

# Example Usage:
# obj = LockedClass()
# obj.first_name = "Alex"  # This will work
# obj.last_name = "Smith"  # This will raise an AttributeError
# print(obj.__dict__)      # This will raise an AttributeError
