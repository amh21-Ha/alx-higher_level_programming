#!/usr/bin/python3

def element_at(my_list, idx):
    if idx > (len(my_list) - 1) and idx < 0:
        return None
    else:
        element = my_list[idx]
        return element
