#!/usr/bin/python3

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    # ... [rest of the class definition with properties and methods]

    def __del__(self):
        print("Bye rectangle...")

# Correct usage in a loop
for i in range(10):
    m1 = Rectangle(2, 4)
    del m1  # Explicitly delete each instance to trigger __del__
