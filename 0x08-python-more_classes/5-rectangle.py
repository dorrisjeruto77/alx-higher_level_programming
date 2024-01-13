#!/usr/bin/python3

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    # [rest of the class definition with properties and methods]

    def __del__(self):
        print("Bye rectangle...")

# Usage Example 1
try:
    myrectangle = Rectangle(2, 4)
    del myrectangle
    print(myrectangle.width)  # This will raise an error
except Exception as e:
    print(f"[{e.__class__.__name__}] {e}")

# Usage Example 2 (Loop)
for i in range(10):
    m1 = Rectangle(2, 4)
    del m1
