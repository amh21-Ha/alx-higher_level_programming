#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [[c ** 2 for c in r] for r in matrix]
    return new_matrix
