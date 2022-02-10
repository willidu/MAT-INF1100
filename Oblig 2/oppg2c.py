import numpy as np
import matplotlib.pyplot as plt

# Definerer f, Tnf op Rnf
def f(x):
    return 1 / x ** 2

def Tnf(x, n):
    s = 0
    for k in range(n+1):
        s += (-1)**k * (k+1) * (x-1)**k
    return s

def Rnf(x, c, n):
    return (-1)**(n+1) * ((n+2)/c**(n+3)) * (x-1)**(n+1)

# Plotter f og Tnf for n fra  0 til 4
x = np.linspace(1, 1.25, 1000)
plt.plot(x, f(x), label='f(x)')

for n in range(5):
    plt.plot(x, Tnf(x, n), label=f'n={n}')

plt.title(r'Taylor approximation of f(x)=$\frac{1}{x^2}$')
plt.grid()
plt.xlim(1, 1.25)
plt.legend()
# plt.show()

# Skal regne ut feil i approksimasjon
# Velger x = 1.25 siden der er feilen størst
x = 1.25
c = 1
n = 0
error = Rnf(x, c, n)

while abs(error) > 0.02:
    n += 1
    error = Rnf(x, c, n)

print(error, n)

for n in range(20):
    print(n, Rnf(x, c, n))

# Kort testfunksjon for å sjekke at n-verdien vi har funnet er riktig
def test_error():
    x = 1.25
    c = 1.0
    for n in range(1000, 3, -1):
        expected = f(x) - Tnf(x, n)
        tolerance = 0.02
        calculated = Rnf(x, c, n)
        sucess = abs(expected-calculated) < tolerance
        msg = f'Test failed at n = {n}'
        assert sucess, msg

test_error()