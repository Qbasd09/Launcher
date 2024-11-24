import math
import csv

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
    Cd = float(i[2])
    
    F_lift = 1000 
    v = 8


    while abs(F_g) < F_lift:

        RadAlpha = math.radians(Alpha)
        vVer = v * math.sin(RadAlpha)
        vHor = v * math.cos(RadAlpha)
        F_lift = Cl * ro * vHor**2 * A * 0.5
        
        v -= 0.01

    a = F_lift/m
    a_v = abs(g+a)
    
    if Alpha == 0:
        F_lift0 = F_lift
        a_0 = a
        a_v0 = a_v

    h0 = 1.5
    h = 0
    tLaunchAngle = 0.5

    h1 = h0 + vVer * tLaunchAngle - 0.5 * a_v * tLaunchAngle**2
    vVer1 = 0
    d1 = vHor * tLaunchAngle

    d = vHor*((vVer1 + (vVer1**2 + 2 * h1 * a_v0)**0.5)/a_v0) + d1

    print(f"{Alpha:.2f}, {h1:.2f}, {a_v:.2f}, {h1:.2f}, {d1:.2f}, {d:.2f}, {vHor:.2f}, {vVer:.2f}")