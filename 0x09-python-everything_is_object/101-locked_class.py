#!/usr/bin/python3

class LockedClass:
    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError("Cannot create new instance attributes except 'first_name'")
        super().__setattr__(name, value)
