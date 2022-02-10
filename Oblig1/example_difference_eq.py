# x_n = 1/4 * x_n-1 + 5/4 * x_n-2

xpp = 190
xp = 260
for i in range(21):
    x = xp/4 + xpp * 5/4
    print(i+2, x)
    xpp = xp
    xp = x
