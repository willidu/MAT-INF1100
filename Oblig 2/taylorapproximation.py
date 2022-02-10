import numpy as np
import sympy as sy
from sympy import N

def taylor_approximation(f, a, n):
    """
    Returns the Taylor approximation Tnf(x) in point a
    :param f: function to be approximated
    :param a: point
    :param n: order of approximation
    :return:Tnf(x)
    """
    from math import factorial
    from sympy import Symbol

    x = Symbol('x')

    def prime(f, x):
        """ Calculates derivative in point """
        h = 1e-12
        return (f(x+h) - f(x)) / h

    Tnf = f(a)  # Initial sum k = 0
    for k in range(1, n+1):
        term = prime(f, a) / factorial(n) * (x - a)**2
        # Her mangler det en del, typ def oppdatere f med f'
        Tnf += term
    return Tnf

def f(x):
    from sympy import cos
    return cos(x)

for i in range(10):
    print(i, taylor_approximation(f, np.pi/4, i))