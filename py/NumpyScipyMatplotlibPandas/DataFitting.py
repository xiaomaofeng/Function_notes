import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def func(x, a, b, c):
    return a * np.exp(-b * x) + c


x = np.linspace(0, 4, 50)
y = func(x, 2.5, 1.3, 0.5)
ydata = y + 0.2 * np.random.normal(size=len(x))
popt, pcov = curve_fit(func, x, ydata)
plt.plot(x, ydata, 'b*')
plt.plot(x, func(x, popt[0], popt[1], popt[2]), 'r-')
plt.title('$f(x)=ae^{-bx}+c$ curve fitting')
#plt.title('a * np.exp(-b * x) + c curve fitting')
plt.show()

