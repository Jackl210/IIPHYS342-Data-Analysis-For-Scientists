# -*- coding: utf-8 -*-
"""
Position Calculation for Olympic thing

EQUATION IN USE: Y(position) = Ysub0(Starting position) + Vsub0(Velocity) * T(time) - 1/2G(gravitational acceleration) * T**2
Short Version:
    y = y0 + v * t - 1/2 * g * t**2
    
VELOCITY EQUATION:
    v - g * t
    
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

speed = v - (g * t) #speed equation

#-----------------------------------Individual Graph Commands
plt.style.use('dark_background') #Style
'''
plt.figure()    #-------------------Graph figure 1
plt.plot(
    t,y, 
    color = "red", 
    linestyle='dotted', 
    marker = "o", 
    alpha = 1,
    markersize = 0.25
    ) 
plt.title("Graph1-Jack")            #Graph title 1
plt.xlabel("Time")                  #Graph axis 1
plt.ylabel("Position")              #Graph axis 2


plt.figure()    #-------------------Graph figure 2

plt.plot(t,speed,
    color = "#008080", 
    linestyle='dotted', 
    marker = "o", 
    alpha = 1,
    markersize = 0.25
    )
plt.title("Graph2-Jack")            #Graph title 2
plt.xlabel("Time")                  #Graph axis 1
plt.ylabel("Speed")              #Graph axis 2

'''
#-----------------------------------Subplot Graph Commands


fig, (ax1, ax2) = plt.subplots(2, sharex=True)               #Plotting subplots
fig.suptitle('Vertically stacked subplots')     #Figure Name for subplots
ax1.plot(                                       #Subplot 1 .plot
    t,y, 
    color = "red", 
    linestyle='dotted', 
    marker = "o", 
    alpha = 1,
    markersize = 0.25)
ax1.set_title("Graph1-Jack")            #Graph title 1
ax1.set_xlabel("Time")                  #Graph axis 1
ax1.set_ylabel("Position")              #Graph axis 2


ax2.plot(                                       #Subplot 2 .plot
    t,speed,
    color = "#008080", 
    linestyle='dotted', 
    marker = "o", 
    alpha = 1,
    markersize = 0.25)
ax2.set_title("Graph2-Jack")            #Graph title 2
ax2.set_xlabel("Time")                  #Graph axis 1
ax2.set_ylabel("Speed")                 #Graph axis 2

plt.subplots_adjust(hspace=0.5)
plt.savefig('I:\My Drive\DataAnalysisForSci\Deliverables\pysaves\jumper.jpg', dpi=300)  #Save as file



#########################################################               #########################################################
#########################################################               #########################################################
#########################################################     Notes     #########################################################
#########################################################               #########################################################
#########################################################               #########################################################
#########################################################               #########################################################
"""
GRAPH SYNTAX: 
horizontal, vertical, color = color, linestyle = style of choice, marker = style of choice, alpha = transparency level, markersize = int


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
       
--------------------------------------

TO HAVE TWO PLOTS ON THE SAME GRAPH, PUT EVERYTHING UNDER THE SAME PLT.FIGURE!!!

TO HAVE TWO PLOTS ON TWO GRAPHS, BREAK IT AND ADD A NEW FIGIURE OR SUBPLOT!!!
    
        
"""

#########################################################               #########################################################
#########################################################               #########################################################
#########################################################    Console    #########################################################
#########################################################   Commands    #########################################################
#########################################################               #########################################################
#########################################################               #########################################################

'''
clear
plt.close('all')


'''