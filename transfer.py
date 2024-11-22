import time

L = 2
h = 1.5
targetV = 10
g = 9.81
vPlane = 0
mPlane = 0.035
mCounterweight = 0.2


while vPlane < targetV:
    
    print(h)

    i = L/h

    vmax = (2*mCounterweight*g*h/mPlane)**0.5
    
    t = (2*h/g)**0.5

    vCounterweight = g*t

    vPlane = vCounterweight*i

    print(f"plane v {vPlane} counterv {vCounterweight} vmax {vmax}")

    # time.sleep(0.5)

    if vPlane > vmax:
        print(f"The maximum possible velocity is {vPlaneMax} m/s")
        break
    elif vPlane < targetV:
        h -= 0.01
        vPlaneMax = vPlane
        vCounterweightMax = vCounterweight
        vPlane = 0
        vCounterweight = 0


