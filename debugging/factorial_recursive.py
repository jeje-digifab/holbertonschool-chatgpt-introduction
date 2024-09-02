#!/usr/bin/python3
import sys


def factorial(n):
    """
    Computes the factorial of a given integer.

    Parameters:
    n (int): The integer for which to compute the factorial.

    Returns:
    int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


"""
Retrieve the command-line argument, calculate the factorial,
and print the result
"""
f = factorial(int(sys.argv[1]))
print(f)
