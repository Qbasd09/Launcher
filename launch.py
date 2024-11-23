import math
import csv

v = 9
ro = 1.204
A = 0.03
g = -9.81
m = 0.035
F_g = m * g

with open('alpha_to_cl.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

for i in data:
    Alpha = float(i[0])
    Cl = float(i[1])

    RadAlpha = math.radians(Alpha)
    vHor = v * math.cos(RadAlpha)

    F_lift = Cl * ro * vHor**2 * A * 0.5

    print(f"The lift from angle {Alpha} is {F_lift} N")