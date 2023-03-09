import matplotlib.pyplot as plt
import matplotlib.ticker as tck
ax=plt.subplot(2, 1, 1)
ax.xaxis.set_major_formatter(tck.FormatStrFormatter('%g $\pi$')) #Ads pi as a character to the digits of the x axis
ax.xaxis.set_major_locator(tck.MultipleLocator(base=1.0))
plt.style.use("ggplot")
plt.show()
