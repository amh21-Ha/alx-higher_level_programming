#!/usr/bin/python3

def element_at(list, idx):
    if idx > (len(list) - 1):
        return None
    idx = list[idx]
    if idx < 0:
        return None
    else:
        return idx
