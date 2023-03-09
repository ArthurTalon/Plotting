# Plot the following function for −15 ≤ x ≤ 15: y = [cos(x)] / [1 + (x^2)/5 ]
# Include enough points so that the curve you plot appears smooth. Draw thin gray lines, one horizontal at y = 0 and the other vertical at x = 0. Both lines should appear behind the function. Label the axes x and y.

import numpy as np
import matplotlib.pyplot as plt

xvalues = np.array(np.linspace(-15,15, 120))
yvalues = (np.cos(xvalues))/(1+ ((1/5)*np.power(xvalues,2)))

plt.figure(2, figsize=(6,4))                                #creates the image for the graph
plt.xlabel("x")                                             #Horizontal Axis Title
plt.ylabel("y")                                             #Vertical Axis Title
plt.axhline(color="gray", zorder=-1)                        #set x = 0 line in gray
plt.axvline(color="gray", zorder=-1)                        #set y = 0 line in gray
plt.plot(xvalues, yvalues)                                  #Plots all the values for x and y colectively in the same function
plt.show()                                                  #Allows visual graphics to be seen 
