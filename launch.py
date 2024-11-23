import math

v = 9
ro = 1.204
A = 0.03
g = -9.81
m = 0.035
F_g = m * g
Alpha = 0

while Alpha <= 19:

    Cl = 0.000016666 * Alpha**4 - 0.000634738 * Alpha**3 + 0.000755963 * Alpha**2 + 0.142456 * Alpha + 0.292422
    RadAlpha = math.radians(Alpha)
    vHor = v * math.cos(RadAlpha)

    F_lift = Cl * ro * vHor**2 * A * 0.5

    if Alpha == 0:
        print(f"Lift is {F_lift}")

    Alpha += 0.25