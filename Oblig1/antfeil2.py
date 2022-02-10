from random import random

antfeil = 0; N = 100000

for i in range(N):
    x = random(); y = random(); z = random()  # gir x, y, z tilfeldige tallverdier
    res1 = (x+y) * (y+z)  # resonement 1, bør gi samme svar som res2
    res2 = x*y + x*z + y*y + y*z  # resonement 2
    if res1 != res2:  # res1 skal være lik res2 etter regnereglene
        antfeil += 1  # legger til +1 i antall feil ved oppdaget feil
        x0 = x; y0 = y; z0 = z
        ikkelik1 = res1
        ikkelik2 = res2

print(100. * antfeil/N)  # prosent av i in (N) som ga res1 != res2
print(x0, y0, z0, ikkelik1 - ikkelik2)  # printer siste x og y verdi som ga ulike res1 og res2 verdier