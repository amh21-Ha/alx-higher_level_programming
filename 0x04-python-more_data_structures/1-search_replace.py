#!/usr/bin/python3

def search_replace(my_list, search, replace):
    n_list = []
    for z in range(len(my_list)):
        if my_list[z] == search:
            n_list.append(replace)
        else:
            n_list.append(my_list[z])
    return n_list
