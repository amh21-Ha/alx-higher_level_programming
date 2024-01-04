#!/usr/bin/python3
if __name__ == "__main__":
    """
    Handle basic arithmetic operations.
    """
    import calculator_1 #import add, sub, mul, div
    import sys
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    ops = {"+": calculator_1.add, "-": calculator_1.sub, "*": calculator_1.mul, "/": calculator_1.div}
    if sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
