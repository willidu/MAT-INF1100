"""
Oppgave 1a)
x_n+2 - 4 * x_n+1 - x_n = 0
x_i+2 - 4 * x_i+1 - x_i = 0
x_i - 4 * x_i-1 - x_i-2 = 0
x_i = 4 * x_i-1 + x_i-2
"""
import math

x = [1, 1]
n = 100
for i in range(len(x), n+1):
    x.append(4*x[i-1] + x[i-2])
    print(i, x[i])

