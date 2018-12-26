import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def fun(x):
    return x**2 - 2*x + 3

def fun1(t):
    #res=np.sin(t)
    return 16 * np.sin(t)**3

def fun2(a,b):
    return np.sin(a) + 0.05 * a**2 + np.sin(b) + 0.05 * b**2

x=np.linspace(0, 10,201)
plt.plot(x, fun(x), 'k-')
plt.plot(1, 2, 'ro')

#fig=plt.figure(figsize=(6, 7))
plt.subplot(2,2,1)
t=np.linspace(0, 2*math.pi)
plt.plot(t, fun1(t),'r-')

a, b = np.mgrid[-10:10:100j, -10:10:100j]
fig = plt.figure(figsize=(8, 6))
ax = plt.axes(projection='3d')
#surf = ax.plot_surface(x, y, z, rstride=1,cmap=cm.coolwarm, cstride=1,linewidth=0)
surf = ax.plot_surface(a, b, fun2(a, b),rstride=1, cmap=cm.coolwarm, cstride=1, linewidth= 0)
plt.title('$f(x,y)=sin(x)+0.05x^2+sin(y)+0.05y^2$')
plt.show()
