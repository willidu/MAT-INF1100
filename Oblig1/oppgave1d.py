import math

n = 100

x_b = [1, 2-math.sqrt(5)]
for i in range(len(x_b), n+1):
    x_b.append(4*x_b[i-1] + x_b[i-2])

x_c = [0] * (n + 1)
for i in range(n+1):
    x_c[i] = (2 - math.sqrt(5))**i

for i in range(0, n+1):
    error = abs(x_b[i] - x_c[i])
    print(f"{i:3}, {x_b[i]:10e} {x_c[i]:10e} {error:e}")
