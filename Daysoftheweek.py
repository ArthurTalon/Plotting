
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapz

print("\n*************** Exercise 7.7 ***************")

#integrate the functions

def trapz(f, a, b, tol=1.0e-8, **fparams):
    h = b-a #a value in integral function, b represents b value in integral function.
    s = 0.5*h*(f(a, **fparams) + f(b, **fparams))
    n, e = 1, 1.0
    while e > tol:
        h *= 0.5
        d = 0.0
        for x in np.linspace(a+h, b-h, n):
            d += h * f(x, **fparams)
        s = 0.5 * s + d
        e = abs(abs(d/s) - 0.5)
        n *= 2
    return s, e, int(np.log2(n))
print("\n(a)")

def f(x, c, p):
    return c * x**p

# First integral
print("Integrate x\u00b2 from 2 to 5")
sus, e, n = trapz(f, 2.0, 5.0, **{"c": 1.0, "p": 2})
print(f"s={sus:0.6e}, e={e:0.2e}, n={n:d}")
a = 39.0
print(f"actual error = {(sus - a)/a:0.2e}\n")

print("Integrate 2x\u00b3 from 1 to 5")
s, e, n = trapz(f, 1.0, 5.0, **{"c": 2.0, "p": 3})
print(f"s={s:0.6e}, e={e:0.2e}, n={n:d}")
a = 312.0
print(f"actual error = {(s - a)/a:0.2e}\n")

def g(x, A, k):
    return A * np.sin(k * x)

print("(b)")
# First integral
print("Integrate sin(x) from 0 to pi")
s, e, n = trapz(g, 0.0, np.pi, **{"A": 1.0, "k": 1.0})
print(f"s={s:0.6e}, e={e:0.2e}, n={n:d}")
a = 2.0
print(f"actual error = {(s - a)/a:0.2e}")

# Second integral
print("\nIntegrate 7sin(x/3) from pi/2 to 2pi")
s, e, n = trapz(g, np.pi/2, np.pi*2, **{"A": 7.0, "k": 1.0/3.0})
print(f"s={s:0.6e}, e={e:0.2e}, n={n:d}")
a = 28.686533479473
print(f"actual error = {(s - a)/a:0.2e}")

print("\n(c)")

def g(x, B, w):
    return B * np.exp(-((x / w) ** 2))

# First integral
print("Integrate exp(-x^2) from 0 to 3.5")
s, e, n = trapz(g, 0.0, 3.5, **{"B": 1.0, "w": 1.0})
print(f"s={s:0.6e}, e={e:0.2e}, n={n:d}")
a = 0.8862262668989
print(f"actual error = {(s - a)/a:0.2e}\n")

# Second integral
print("Integrate 4*exp(-(x/2)^2) from 1 to 5")
s, e, n = trapz(g, 1.0, 5.0, **{"B": 4.0, "w": 2.0})
print(f"s={s:0.6e}, e={e:0.2e}, n={n:d}")
a = 3.3966821376379
print(f"actual error = {(s - a)/a:0.2e}")


print("\n*************** Exercise 7.10 ***************")

def day_of_week(y, m, d):
    weekday = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"}
    y = y - int((14-m)/12)
    x = y + int(y/4) - int(y/100) + int(y/400)
    m = m + 12 * int((14-m)/12) - 2
    d = (d + x + int((31 * m) / 12)) % 7
    return weekday[d]

dates = [(1700, 1, 1),(1776, 7, 4),(1777, 4, 30),(1813, 1, 28),(1861, 3, 4),(10879, 3, 14),(1918, 5, 11),(1969, 7, 20),(1980, 2, 29),(1989, 11, 9),(2009, 1, 20)]
print("month   day   year")
for date in dates:
    print("{0:2d}    {1:2d}   {2:4d}   {3}".format(date[1], date[2], date[0], day_of_week(date[0], date[1], date[2])))

y = int(input("Input year (1700 or later): "))
if y < 1700:
    raise ValueError('Year before 1700')
m = int(input("Input month (1-12): "))
if 0 > m or m > 12 :
    raise ValueError('Month not in range')
d = int(input("Input day (1-31): "))
if 0 > d or d > 31:
    raise ValueError('Day not in range')
if m in [4, 6, 9, 11] and d > 30:
    raise ValueError('Day not in range')
if m == 2 and d > 29:
    raise ValueError('Day not in range')
print(day_of_week(y, m, d))

print("\n************** Exercise 8.6 ***************")

file = open("C:/Users/talon/Documents/PyScripts/falling_ball_data.txt")

for i in range(4):                                          #Skips first 5 lines
    line = file.readline()

t = []                                                      #Array of t values from file
d = []                                                      #Array of d values from file
dy = []                                                     #Array of uncertainties values from file
for line in file.readlines():                               #Imports data to be used from file
    currentline = line.split()
    t.append(float(currentline[0]))
    d.append(float(currentline[1]))
    dy.append(float(currentline[2])) 


fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 14), sharex=True)
#ax1 = fig.add_subplot(2, 2, 1)
ax1.set_ylabel("distance (m)")
ax1.set_xlabel("time (s)")
ax1.errorbar(t,d, fmt='oC1', label='data')

#ax2 = fig.add_subplot(2, 2, 2)

o=1
vo = [0]
while o<len(t):
    # if d[n]==0:
    #     vo.append(0)
    #     n+=1
    #else:
    v = ((d[o])-(d[o-1]))/((t[o])-(t[o-1]))
    vo.append(v)
    o = o+1


o=1
va = [0]
#for o in range(len(t)): better efi
while o<len(t):
    v = ((vo[o])-(vo[o-1]))/((t[o])-(t[o-1]))
    va.append(v)
    o=o+1

#ax3 = fig.add_subplot(2, 1, 2)
ax3.axhline(9.8, label="9.8 m/s\u00b2", color="C0")
# plt.plot(label="9.8 m/s\u00b2") #s\u00b2
plt.legend(loc="upper right", title="")

ax3.set_xlabel("time (s)")
ax3.set_ylabel("acceleration (m/s\u00b2)")
po = np.delete(t,0)
po2 = np.delete(po,0) 

pi = np.delete(va,0)
pi2 = np.delete(pi,0)

pu= np.delete(dy, 0)
pu2=np.delete(pu,0)


#ax3.errorbar(po2, pi2, fmt='^C1', label='data', yerr=pu2, ecolor="C1")

xdata, ydata, yerror = np.loadtxt("C:/Users/talon/Documents/PyScripts/falling_ball_data.txt", skiprows = 4, unpack= True)

#setting up velocity calc
vel_setup1 = []
for x, y in zip(xdata[0::], xdata[1::]):
    vel_setup1.append(y-x)
vel_setup2 = []
for x, y in zip(ydata[0::], ydata[1::]):
    vel_setup2.append(y-x)
vel = [i / j for i, j in zip(vel_setup2, vel_setup1)]
vel_error = []
for x, y in zip(yerror[0::], yerror[1::]):
    vel_error.append(np.sqrt(x**2 + y**2))

#setting up acceleration calc
acc_setup1 = []
for x, y in zip(xdata[1::], xdata[2::]):
    acc_setup1.append(y-x)
acc_setup2 = []
for x, y in zip(vel[0::], vel[1::]):
    acc_setup2.append(y-x)
acc = [i / j for i, j in zip(acc_setup2, acc_setup1)]
acc_error = []
for x, y in zip(vel_error[0::], vel_error[1::]):
    acc_error.append(np.sqrt(x**2 + y**2))

# fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 14), sharex=True)
# x = np.linspace(0, 10, 100)
# ax1.errorbar(xdata, ydata, fmt="o", yerr=yerror, ecolor="blue")
# ax1.set_xlabel("time (s)")
# ax1.set_ylabel("displacement (m)")

x1 = []
for x, y in zip(xdata[0::], xdata[1::]):
    x1.append((y-x)/2 + x)
ax2.errorbar(x1, vel, fmt="sC1", yerr=vel_error, ecolor="orange")
ax2.set_xlabel("time (s)")
ax2.set_ylabel("velocity (m/s)")

x2 = []
for x, y in zip(x1[0::], x1[1::]):
    x2.append((y-x)/2 + x)
ax3.errorbar(x2, acc, fmt="^C1", yerr=acc_error, ecolor="orange")
ax3.set_xlabel("time (s)")
ax3.set_ylabel("acceleration (m/s\u00b2)")
fig.savefig("C:/Users/talon/Documents/PyScripts/PlotGraphs.pdf") #Creates a pdf file and stores designated graph

print("\n************** Exercise 8.8 ***************")

def pmgauss(x, y):
    function = 10*np.cos((1/3)*x*y+5)*np.sin(x)-2*np.cos(x)
    return function

x = np.linspace(-2.5,2.5,100, endpoint=False)
y = np.linspace(-2.5,2.5,100, endpoint=False)

X, Y = np.meshgrid(x, y)
Z = pmgauss(X, Y)

fig, ax = plt.subplots(figsize=(9.5, 6.5))
#lev2 = np.arange(14, 15, 0.3)
CS=ax.contour(X, Y, Z, 14, colors="k")

ax.clabel(CS, fontsize=9, fmt="%0.1f")
ax.set_title('Contour Plot')
ax.set_xlabel("x")
ax.set_ylabel("y")

fig.savefig("C:/Users/talon/Documents/PyScripts/PlotContour.pdf") #Creates a pdf file and stores designated graph
plt.show() #Plots all Graphs in All problems
