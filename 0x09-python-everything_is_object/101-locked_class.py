#!/usr/bin/python3

"""
Module documentation: LockedClass module
This module provides the LockedClass class which restricts attribute creation.
"""

class LockedClass:
    """
    A class that only allows creating an attribute named 'first_name'.
    Any attempt to set other attributes will result in an AttributeError.
    """

    def __setattr__(self, name, value):
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"Can't set attribute '{name}'")

# Example Usage:
# obj = LockedClass()
# obj.first_name = "Alex"  # This will work
# obj.last_name = "Smith"  # This will raise an AttributeError
# print(obj.__dict__)      # Will display the dictionary of obj
