#!/usr/bin/python3

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    # [rest of the class definition with properties and methods]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Bye rectangle...")

# Usage Example
with Rectangle(2, 4) as myrectangle:
    # Do something with myrectangle
    pass  # This pass statement is just a placeholder
