import matplotlib.pyplot as plt
import numpy as np

x_min = 0.05
x_max = 1.95
points = 1000
x = np.linspace(x_min, x_max, points)

def f(x):
    return np.log(x)

def T1f(x):
    return (x-1)

def T2f(x):
    return T1f(x) - 1/2 * (x-1) ** 2

def T3f(x):
    return T2f(x) + 1/3 * (x-1) ** 3

plt.plot(x, f(x), label='ln(x)')
plt.plot(x, T1f(x), label='n=1')
plt.plot(x, T2f(x), label='n=2')
plt.plot(x, T3f(x), label='n=3')

plt.title('Taylor approximation of ln(x)')
plt.xlim(x_min, x_max)
plt.legend(loc='lower right')
plt.grid()
plt.show()
