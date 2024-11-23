import math

v = 9.67
ro = 1.204
A = 0.309
g = -9.81
m = 0.035
Alpha = -2

while Alpha <= 19:

    Cl = 0.000016666 * Alpha**4 - 0.000634738 * Alpha**3 + 0.000755963 * Alpha**2 + 0.142456 * Alpha + 0.292422
    RadAlpha = math.radians(Alpha)
    vHor = v * math.cos(RadAlpha)

    F_lift = Cl * ro * vHor**2 * A * 0.5

    print(vHor)

    print(f"For an angle {Alpha} degrees, the lift is {F_lift} N, cl {Cl}")

    Alpha += 0.25