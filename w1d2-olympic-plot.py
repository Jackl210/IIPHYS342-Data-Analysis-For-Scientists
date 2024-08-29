# -*- coding: utf-8 -*-
"""
Position Calculation for Olympic thing

EQUATION IN USE: Y(position) = Ysub0(Starting position) + Vsub0(Velocity) * T(time) - 1/2G(gravitational acceleration) * T**2
Short Version:
    y = y0 + v * t - 1/2 * g * t**2
    
"""

#-----------------------------------LIBRARIES: 
import numpy as np
import matplotlib.pyplot as plt


#-----------------------------------VARIABLES:
y0 = 0.7 #m Start point in meters
v = 4.4 #m/s Speed of jumper
g = 9.8 #m/s^2 Gravity on earth


#-----------------------------------TIME:
#t = 0.3 #seconds
t = np.arange(0,1,0.01) 


#-----------------------------------RUN IT THIS WAY:
y = y0 + (v * t) - (1/2 * g) * (t**2)


#-----------------------------------Graph Commands
plt.style.use('dark_background') 
plt.figure()
plt.title("Graph1-Jack")
plt.xlabel("Time")
plt.ylabel("Position")
plt.plot(
    t,y, color = "red", 
    linestyle='dotted', 
    marker = "o", 
    alpha = 1,
    markersize = 0.25,
    
    ) 
#horizontal, vertical, color = color, linestyle = style of choice, marker = style of choice, alpha = transparency level, markersize = int



#-----------------------------------Notes:
"""
Linestyles are as follows:
    Using linestyle Argument:
        Solid
        Dashed
        Dotted
        Dashdot
        None
    Using ls Argument:
        ‘-‘
        ‘:’
        ‘–‘
        ‘-.’
        ‘ ‘
        
EXAMPLE CODE FROM ONLINE: 
# plotting data 
plt.plot(xdata, ydata, linestyle='dotted') 

--------------------------------------

Marker Settings are as follows:
    use argument "marker = "
        ".": point
        "o": circle
        "s": square
        "^": triangle
        "v": upside down triangle
        "+": plus
        "x": X
        
    adjusting size of marker: use argument "s = "
        insert size after =
        
    set color, use argument "c = "
        insert color after =
        
    
        
"""