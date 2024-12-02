import math
import csv
import numpy as np
import matplotlib.pyplot as plt

rho = 1.204
A = 0.03325
m = 0.035
coef = rho * A /(2 * m)

with open('alpha_to_cl.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

angdist = []

for i in data:
    Alpha = float(i[0])
    Cl = float(i[1])
    Cd = float(i[2])
 
    if Alpha == 0:
        Cd0 = Cd

    v = 6.43

    RadAlpha = math.radians(Alpha)
    vVer = v * math.sin(RadAlpha)
    vHor = v * math.cos(RadAlpha)
    vHor1 = vHor

    h0 = 1.5
    h = 0
    tLaunchAngle = 1

    tl0 = 0.001 * tLaunchAngle
    tl1 = tl0
    d1 = 0

    while tl0 <= tLaunchAngle:
        tl0 += 0.001 * tLaunchAngle
        vHor1 = 1 / (coef * tl0 * Cd + 1/vHor)
        d1 = vHor1 * tl1 + d1

    # d1 = vHor * tLaunchAngle
    h1 = h0 + vVer * tLaunchAngle

    vHor2 = 1 / (coef * tLaunchAngle * Cd + 1/vHor)
    vHor3 = vHor2
    vVer1 = 0
    a = 1

    t = (2 * h1/a)**0.5

    t0 = 0.001 * t
    t1 = t0
    d2 = 0

    while t0 <= t:
        t0 += 0.001 * t
        vHor2 = 1 / (coef * t0 * Cd0 + 1/vHor3)
        d2 = vHor2 * t1 + d2

    d = d1 + d2

    angdist.append([Alpha, d])

arr = np.array(angdist)

plt.plot(arr[:, 0], arr[:, 1])
plt.title(f"Launch distance at v = {v} m/s")
plt.ylabel("Distance ($m$)")
plt.xlabel("Angle$\degree$")
plt.grid(True)
plt.savefig('graph6.png', dpi=1000)