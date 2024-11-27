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
 
    v = 9.67

    RadAlpha = math.radians(Alpha)
    vVer = v * math.sin(RadAlpha)
    vHor = v * math.cos(RadAlpha)
    
    h0 = 1.5
    h = 0
    tLaunchAngle = 1

    d1 = vHor * tLaunchAngle
    h1 = h0 + vVer * tLaunchAngle

    vHor1 = 1 / (coef * tLaunchAngle * Cd + 1/vHor)
    vVer1 = 0
    a = 1

    t = (2 * h1/a)**0.5

    t0 = 0.01 * t
    t1 = t0
    d2 = 0

    while t0 < t:
        t0 += 0.01 * t
        vHor1 = 1 / (coef * t0 * Cd + 1/vHor1)
        d2 = vHor1 * t1 + d2

    d = d1 + d2

    angdist.append([Alpha, d])

arr = np.array(angdist)

plt.plot(arr[:, 0], arr[:, 1])
plt.title(f"Launch distance at v = {v} m/s")
plt.ylabel("Distance ($m$)")
plt.xlabel("Angle$\degree$")
plt.grid(True)
plt.savefig('graph.png', dpi=1000)