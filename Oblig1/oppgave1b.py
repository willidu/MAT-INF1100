import math
import numpy as np
import matplotlib.pyplot as plt

"""
Oppgave 1b
"""
x = [1, 2-math.sqrt(5)]
n = 100
for i in range(len(x), n+1):
    x.append(4*x[i-1] + x[i-2])
    print(f"{i:3} {x[i]:10e}")

x2 = x[:30]
n2 = np.linspace(0, 30, 30)
plt.plot(n2, x2)
plt.show()
