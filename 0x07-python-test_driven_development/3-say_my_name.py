# This module defines a function that prints a person's name
def say_my_name(first_name, last_name=""):
    """
    This function prints a person's name in the format "My name is
    <first name> <last name>".
    If the last name is not provided, it prints only the first name.
    It raises a TypeError exception if the first name or the last name
    is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
