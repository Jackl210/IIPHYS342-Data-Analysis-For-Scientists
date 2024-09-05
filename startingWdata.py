# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 12:04:00 2024

@author: Jack

Beginning with data: Importing a .csv

"""

#-----------------------------------LIBRARIES: 
    
import numpy as np     #Number shit
import matplotlib.pyplot as plt     #Graphing
import pandas as pd     #Dealing with data


#-----------------------------------DEFINE FILES AND DIRECTORIES:
    
fildir = 'I:\My Drive\DataAnalysisForSci\py-data'     #Where the file lives
file = fildir + '\GlobalTemp.csv'     #Directory + name


#-----------------------------------VARIABLES:


#-----------------------------------READ IN THE DATA:

data = pd.read_csv(file)


#-----------------------------------PLOTS:

plt.figure()
plt.suptitle('Comparisons:')     #Figure Name for subplots


plt.subplot(3,1,1)#-----------------------------------SUBPLOT 1
plt.plot(
    data['years'],
    data['temp'],
    color = "red", 
    linestyle='solid', 
    marker = "v", 
    alpha = 1,
    markersize = 0.25,
    label = "Years x Temp"
    )  
plt.title("Years x Temp")
plt.xlabel("Years")
plt.ylabel("Temp (C)") 

plt.subplot(3,1,2)#-----------------------------------SUBPLOT 2
plt.plot(
    data['years'],
    data['human_impact_factor'],
    color = "orange", 
    linestyle='solid', 
    marker = "v", 
    alpha = 1,
    markersize = 0.25,
    label = "Years x Human Impact"
    )
plt.title("Years x Human Impact")
plt.xlabel("Years")
plt.ylabel("Human Impact")     

plt.subplot(3,1,3)#-----------------------------------SUBPLOT 3
plt.plot(
    data['temp'],
    data['human_impact_factor'],
    color = "yellow", 
    linestyle='solid', 
    marker = "v", 
    alpha = 1,
    markersize = 0.25,
    label = "Temp x Human Impact"
    )
plt.title("Temp x Human Impact")
plt.xlabel("Temp (C)")
plt.ylabel("Human Impact")  



plt.subplots_adjust(hspace=2)
plt.savefig('I:\My Drive\DataAnalysisForSci\Deliverables\pysaves\h-impact.jpg', dpi=300)  #Save as file



#-----------------------------------SCATTER PLOTS:

plt.figure()
plt.suptitle('Scatterplot 1:')     #Figure Name for subplots

plt.scatter(data['years'], data['temp'], c = data['human_impact_factor'], cmap = "Oranges")
plt.xlabel("Years")
plt.ylabel("Temp (C)") 

cbar = plt.colorbar()
cbar.set_label('Human Impact Factor')


plt.savefig('I:\My Drive\DataAnalysisForSci\Deliverables\pysaves\scatter1.jpg', dpi=300)  #Save as file




# iloc is index location:       print(data.iloc[3])
    