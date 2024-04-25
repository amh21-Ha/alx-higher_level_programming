#!/usr/bin/python3

""" """


def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low <= high:
        mid = (low + high) // 2
        """ Check if mid is a peak"""
        if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and
        (mid == len(list_of_integers)) - 1 or list_of_integers[mid + 1]
        <= list_of_integers[mid]:
            return list_of_integers[mid]
        """If the element at mid is not a peak and the left neighbor is greater
        than mid, then there must be a peak on the left side"""
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            high = mid - 1
        """If the element at mid is not a peak and the right neighbor is
        greater than mid, then there must be a peak on the right side"""
        else:
            low = mid + 1

    return None
