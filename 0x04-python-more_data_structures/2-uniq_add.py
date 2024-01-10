#!/usr/bin/python3

def uniq_add(my_list=[]):
    n = set(my_list)
    res = 0
    for i in n:
        res += i
    return res
