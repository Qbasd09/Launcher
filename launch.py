import math
import csv
import numpy as np
import matplotlib.pyplot as plt

ro = 1.204
A = 0.03
m = 0.035
coef = ro * A /(2 * m)

with open('alpha_to_cl_full.csv', newline='') as f:
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

    d = vHor1 * t + d1

    angdist.append([Alpha, d])

arr = np.array(angdist)

plt.plot(arr[:, 0], arr[:, 1])
plt.ylabel("Distance $m$")
plt.xlabel("Angle")
plt.grid(True)
plt.savefig('graph.png')