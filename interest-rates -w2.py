"""
Compound interest graph comparison hw

EQUATION IN USE:
    bankX = the Amount of money in your account
    P = Principal, so the money you started with
    r= the annual interest rate as a decimal number
    n=the number of times the interest is compounded in a year (quarterly = 4, monthly = 12)
    t= time in decimal years
    
    bank1 = P*(1+Rate_1/n1)**(n1*time)
    
    
"""

#-----------------------------------LIBRARIES: 
import numpy as np
import matplotlib.pyplot as plt


#-----------------------------------VARIABLES:
A = 1     #Amount of money in my account
P = 10000     #Principal, so money I started with
r = 3     #Annual interest rate as a decimal number
n4 = 4     #Number of times the interest is compounded in a year quarterly
n12 = 12     #Number of times the interest is compounded in a year monthly
t = 5     #Time in decimal years
Rate_1 = .03875
Rate_2 = .06

n1 = 4
n2 = 12
statement = "Bank 1, has an interest rate of 3.875%  (r= 0.03875) & compounds quarterly (n=4) \n\nBank 2, has an interest rate of 3.6. (r= 0.06). &  compounds monthly (n=12)"
print(statement)
#-----------------------------------TIME:

time = np.arange(0,40,0.01) 

#-----------------------------------RUN IT THIS WAY:

bank1 = P*(1+Rate_1/n1)**(n1*time)     #Equation for compounding interest
bank2 = P*(1+Rate_2/n2)**(n2*time)     #Equation for compounding interest



#-----------------------------------Subplot Graph Commands
plt.style.use('dark_background') #Style


fig, (ax1, ax2) = plt.subplots(2, sharex=True, sharey = True)               #Plotting subplots
fig.suptitle('Bank Assessments: Why I chose Bank 2')     #Figure Name for subplots
ax1.plot(                                       #Subplot 1 .plot
    time,bank1, 
    color = "red", 
    linestyle='solid', 
    marker = "o", 
    alpha = 1,
    markersize = 0.25)
ax1.set_title("Bank 1")            #Graph title 1
ax1.set_xlabel("Time (Years)")                  #Graph axis 1
ax1.set_ylabel("Amount")              #Graph axis 2
#plt.ylim(0,50000)
#plt.yticks(range(0,50000,5000))     #Starting number, ending number, and interval
#plt.grid(axis = "y")     #Gridlines




ax2.plot(                                       #Subplot 2 .plot
    time,bank2,
    color = "#008080", 
    linestyle='solid', 
    marker = "o", 
    alpha = 1,
    markersize = 0.25)
ax2.set_title("Bank 2")            #Graph title 2
ax2.set_xlabel("Time (Years)")                  #Graph axis 1
ax2.set_ylabel("Amount")                 #Graph axis 2

plt.subplots_adjust(hspace=0.5)
plt.savefig('I:\My Drive\DataAnalysisForSci\Deliverables\pysaves\jumper.jpg', dpi=300)  #Save as file

#-----------------------------------Single graph

plt.figure()
plt.plot(
    time,bank1, 
    color = "red", 
    linestyle='solid', 
    marker = "o", 
    alpha = 1,
    markersize = 0.25,
    label = "Bank 1")

 
plt.plot(
    time,bank2,
    color = "#008080", 
    linestyle='solid', 
    marker = "o", 
    alpha = 1,
    markersize = 0.25,
    label = "Bank 2")
plt.legend()
plt.savefig('I:\My Drive\DataAnalysisForSci\Deliverables\pysaves\jumper2.jpg', dpi=300)  #Save as file


#-----------------------------------Notes/comments
'''
1) I totally skipped the copy paste part so I may have messed up but it's 3am rn so screw it
2) Figure has two subplots, one on other. Labels match assignment.
3) Colors are not default, I like the dark color scheme, and I went with Red and Teal with blackout style 'dark_background'
4) Linestyle is solid because everything else looked like hell on high DPI displays. 
5) X and Y axis are labelled on both graphs. They are also set to share axis to display scale. 
6) Subplots are labelled according to their bank number. 
7) I would personally use bank 2, as 3.6% compounding monthly will rapidly outgrow 3.875% compounded quarterly. 
8) Already had a suptitle onboard, check prior code. 


'''
