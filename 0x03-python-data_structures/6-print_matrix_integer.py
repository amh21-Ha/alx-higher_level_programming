#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for c in range(len(line)):
            print(
                "{:d}".format(line[c]),
                end="" if c == len(line) - 1 else " ")
        print("")
