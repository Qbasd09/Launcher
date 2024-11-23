import math
import csv
import numpy as np

v = 9.67
ro = 1.204
A = 0.03
g = -9.81
m = 0.035
F_g = m * g
coef = ro * A /(2 * m)


with open('alpha_to_cl.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


for i in data:
    Alpha = float(i[0])
    Cl = float(i[1])
    Cd = float(i[2])
    RadAlpha = math.radians(Alpha)
    vHor = v * math.cos(RadAlpha)
    
    t = np.linspace(0, 50, 500)

    def vHor_t(Cd, t):
        speed = 1 / (coef * t * Cd + 1/vHor)
    
        return speed    

    def F_lift(Cl, t):
        lift = Cl * ro * vHor_t(Cd, t)**2 * A * 0.5

        return lift
    
    a_vertical = g + F_lift(Cl,t)/m

    print(f"the vertical acceleration {a_vertical}")