# Transfer Ratio

## Calculation Concept

To calculate whether a launching velocity is possible, I will use conservation of energy to see the maximum velocity that the plane can achieve, see the maximum possible transfer ratio for a counterweight height, find the velocity of the counterweight at the bottom of its fall, and then using the transfer ratio find the velocity of the plane. Comparing the two velocities will show whether the velocity is possible. All values will be brute forced.

## Calculation variables

Runway length $L = 2 ~ m$
Counterweight height $h \in (0, 1.5]$ can be any value in range
Maximum transfer ratio $i_{max}=\frac{L}{h}$
The formulas $v_{c}=gt$, and $h=\frac{1}{2}gt^2$ will be used to find the velocity of the counterweight falling from a certain height. 
Using the transfer ratio $v_{p} = iv_{c}$
Using conservation of energy $m_{c}gh=\frac{1}{2}m_{p}v_{pmax}^2 \implies v_{pmax}=\sqrt{\frac{2m_{c}gh}{m_{p}}}$ 
If $v_{p} < v_{pmax}$ then the velocity is possible

Target velocity $v_{p} = 10 ~ \frac{m}{s}$

As seen from transfer.py, the target velocity is unachievable, the launch velocity for all further calculations is $8 ~ m/s$, the reason will be explained in the next section.