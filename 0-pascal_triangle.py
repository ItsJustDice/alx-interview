#!/usr/bin/python3
""" Pascal Triangle """

def pascal_triangle(n):
    """Create function def pascal_triangle(n):
    returns a list of lists of integers representing 
    Pascal triangle of n
    """
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            res.append(level)
    return res
