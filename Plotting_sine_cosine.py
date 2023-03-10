import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck

f,ax=plt.subplots(figsize=(20,10))                      #Creates Image 3 parameters
x= np.linspace(-3*np.pi, 3*np.pi,120)
y=np.sin(x/3)                                           #Function sin(x)
k=np.cos(x/3)                                           #Function cos(x) for the given parameters 
ax.plot((x)/(np.pi),k, '-C0')
ax.plot((x)/(np.pi),y, '-C1')
plt.plot( "-C0", label="Cosine")
plt.legend(loc="upper right", title="")
plt.plot( "C1", label="Sine")
plt.legend(loc="upper right", title="")
plt.axhline(color="gray", zorder=-1)
plt.axvline(color="gray", zorder=-1)

plt.figure(2)

plt.show()
