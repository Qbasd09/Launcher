L = 2
h = 1.5
targetV = 10
g = 9.81
vPlane = 0
mPlane = 0.035
mCounterweight = 0.2

while vPlane < targetV:

    i = L/h

    vmax = (2*mCounterweight*g*h/mPlane)**0.5
    
    t = (2*h/g)**0.5

    vCounterweight = g*t

    vPlane = vCounterweight*i

    if vPlane > vmax:
        print(f"The maximum possible velocity is {vPlaneMax:.2f} m/s")
        print(f"When i = {iMax:.2f} and h = {h:.2f} m")
        break
    elif vPlane < targetV:
        hMax = h
        iMax = i
        h -= 0.01
        vPlaneMax = vPlane
        vCounterweightMax = vCounterweight
        vPlane = 0
        vCounterweight = 0


