import sys
import math

n, i = sys.argv[1:3]
n = int(n)
i = int(i)


def coefficient(n, i):
    if i > n / 2:
        i = n - i
    s = 1  # Sum
    for j in range(1, int(i) + 1):
        s *= ((n - j + 1) / j)
    print(s)
    s = 1
    for j in range(1, int(i) + 1):
        s *= ((n - i + j) / j)
    print(s)
    return s


coefficient(n, i)
print(f"{math.comb(n, i):e}")
# print(f"{math.comb(int(n), int(i)):e}")
# print(type(coefficient(n, i)))
# print(f"{coefficient(n, i):.16e}")
# r = abs((math.comb(int(n), int(i)) - coefficient(n, i))) / abs(math.comb(int(n), int(i)))
# print(f"r = {r:e}")

"""
Terminal> python binomial_coefficient.py 5000 4
2.601042812375000e+13
r = 0.000000e+00

Terminal> python binomial_coefficient.py 1000 500
2.702882409454359e+299
r = 2.475719e-15

Terminal> python binomial_coefficient.py 100000 99940
1.180691979962567e+218
r = 9.957991e-16

b) Ja, dersom telleren i brøken er større en det største flyttallet som maskinen
    kan representere. Da får vi overflow error selv om koeffisienten er mindre.

c) Siden Pascals trekant er symmetrisk:
    if i > n / 2.0:
        i = n - i
"""
