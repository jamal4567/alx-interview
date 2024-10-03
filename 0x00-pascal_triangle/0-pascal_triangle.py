#!/usr/bin/python3
"""
0-pascal_triangle module
"""


def pascal_triangle(n):
    """
    Returns a list of integers representing
    The Pascal Triangle of n,
    returns empty list if n <= 0
    """
    l = []
    if n <= 0:
        return l
    l = [[1]]
    for i in range(1, n):
        tmp = [1]
        for j in range(len(l[i - 1]) - 1):
            curr = l[i - 1]
            tmp.append(l[i - 1][j] + l[i - 1][j + 1])
        tmp.append(1)
        l.append(tmp)
    return l