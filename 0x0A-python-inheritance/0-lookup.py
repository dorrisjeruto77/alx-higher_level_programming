#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
    obj (object): The object for which you want to retrieve attributes and methods.

    Returns:
    list: A list of attribute and method names.
    """
    attributes_and_methods = []
    
    for name in dir(obj):
        if callable(getattr(obj, name)) or not name.startswith("__"):
            attributes_and_methods.append(name)
    
    return attributes_and_methods

if __name__ == "__main__":
    class ExampleClass:
        def __init__(self):
            self.attribute1 = 42

        def method1(self):
            return "Hello, World!"

    obj = ExampleClass()

    # Call the lookup function to get attributes and methods of 'obj'
    result = lookup(obj)

    print(result)
