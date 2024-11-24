import math
import csv
import numpy as np
import matplotlib.pyplot as plt

v = 9.67
rho = 1.204
A = 0.03
g = -9.81
m = 0.035
h0 = 1.5
F_g = m * g
coef = rho * A /(2 * m)

with open('alpha_to_cl.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

for i in data:
    Alpha = float(i[0])
    Cl = float(i[1])
    Cd = float(i[2])
    RadAlpha = math.radians(Alpha)

    vHor = v * math.cos(RadAlpha)
    vVer = v * math.sin(RadAlpha)
   
    t = np.linspace(0, 20, 500)

    def vHor_t(Cd, t):
        speed = 1 / (coef * t * Cd + 1/vHor)
   
        return speed

    def F_lift(Cl, Cd, t):
        lift = Cl * rho * vHor_t(Cd, t)**2 * A * 0.5

        return lift
   
    def vVer_t(vVer, Cl, Cd, t):
        speed = vVer + (g + F_lift(Cl, Cd, t)/m) * t

        return speed
        
    def h(t):
        h = 1.5 + vVer * t + g * t**2 / 2 + coef * Cl /(1.2034725 * Cd) * np.emath.log(t) + 2 * coef * Cl / (1.2034725 * Cd * vHor) * t + coef * Cl / (2 * vHor**2) * t**2
        
        return h

    # plt.figure(figsize=(10, 6))
    # plt.plot(t, h, label=f"$vert(t)$ (Velocity) at {Alpha}", color="green")
    # plt.title("height over time", fontsize=14)
    # plt.xlabel("Time (s)", fontsize=12)
    # plt.ylabel("height", fontsize=12)
    # plt.grid(True)
    # plt.legend(fontsize=12)
    # plt.show()