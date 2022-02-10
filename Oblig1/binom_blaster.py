import math
import sys


def coefficient(n, i):
    s = 1
    for j in range(1, int(i) + 1):
        s *= ((n - i + j) / j)
    return s


for n in range(2, 10000000):
    i = int(n/2 - 1)
    if coefficient(n, i) != math.inf:
        print(coefficient(n, i))
    elif coefficient(n, i) == math.inf:
        print(f"inf reached. n = {n}, i = {i}")
        exit()
    """
    else:
        try:
            print(f"{math.comb(n, i):e}")
        except OverflowError:
            print(f"n = {n}, i = {i}")
            raise OverflowError
"""