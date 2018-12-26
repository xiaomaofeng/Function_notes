import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

x, y = np.mgrid[-5:5:100j, -5:5:100j]
z = x**2 + y**2
fig = plt.figure(figsize=(8, 6))
ax = plt.axes(projection='3d')
surf = ax.plot_surface(x, y, z, rstride=1,cmap=cm.coolwarm, cstride=1,linewidth=0)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.title('3D plot of $z = x^2 + y^2$')
plt.show()

