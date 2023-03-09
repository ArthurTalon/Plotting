# To ascertain how well f (t) models the the y vs. time data, plot f (t) as a smooth line on the same plot. To plot f (t) as a smooth line, you will need to create a new NumPy t array separate from the time data. Make the line for f (t) pass behind the data points

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck

file = open("C:/Users/talon/Documents/PyScripts/lauren_john_data.txt") #Change to your Directory where your file is stored

for i in range(5):                                          #Skips first 5 lines
    line = file.readline()                                  #Reads entire line

t = []                                                      #Array of t values from file
d = []                                                      #Array of d values from file
dy = []                                                     #Array of uncertainties values from file
for line in file.readlines():                               #Imports data to be used from file
    currentline = line.split()                              #Creates a list of all the objects read in the line
    t.append(float(currentline[0]))                         #Ads the first object read in the line to array t
    d.append(float(currentline[1]))                         #Ads the second object read in the line to array d
    dy.append(float(currentline[2]))                        #Ads the third object read in the line to array dy

plt.figure(4, figsize=(6,4))                                        #Creates Image 4 parameters
plt.xlabel("Time (s)") 
plt.ylabel("Position (cm)")
plt.axhline(color="gray", zorder=-1)                                #graph gray lines 
plt.axvline(color="gray", zorder=-1)
plt.errorbar(t,d, fmt='oC1', label='data', yerr=dy, ecolor="gray")  #Plot error bars vertically 
u = np.array(np.linspace(0,40, 42))                                   #random range of numbers to plot the function
firstpart = 3+((1/2)*np.sin((np.pi* np.array(u))/(5)))                              #Function B = y=(3+ sin(pi*t/5)/2)
secondpart = (np.array(u))*(np.power((np.exp(1)),(((-1)*(np.array(u)/10)))))        #Function A = y=t*e^(-t/10)
final  = firstpart*secondpart                                                       #Function B*A
plt.plot(t,d, "oC0")
plt.plot(final, 'C4')
plt.show()
