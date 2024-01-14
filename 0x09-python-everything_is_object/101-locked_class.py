#!/usr/bin/env python3

class LockedClass:
    """
    A class that only allows creating an attribute named 'first_name'.
    """
    def __setattr__(self, name, value):
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"Can't set attribute '{name}'")

# Example Usage:
obj = LockedClass()
obj.first_name = "Alex"  # This will work
obj.last_name = "Smith"  # This will raise an AttributeError
