#!/usr/bin/env python3

class LockedClass:
    __slots__ = ("first_name",)

    def __init__(self, first_name):
        self.first_name = first_name

    def __setattr__(self, attr, value):
        if attr != 'first_name':
            raise AttributeError(f"'LockedClass' object has no attribute '{attr}'")
        super().__setattr__(attr, value)

if __name__ == "__main__":
    # Example usage
    obj1 = LockedClass("Alex")
    obj1.age = 30  # This will raise an AttributeError
