#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if key not in _dictionary:
        a_dictionary[key] = value
    else:
        for z in a_dictionary:
            if z == key:
                a_dictionary[z] = value
    return a_dictionary
