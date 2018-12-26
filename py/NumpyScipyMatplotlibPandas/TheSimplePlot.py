import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 201)
plt.figure(figsize=(3, 3))  # new fig
plt.plot(x, x ** 0.3, 'r--')  # red dashed
plt.plot(x, x - 1, 'k-')  # continue plot
plt.plot(x, np.zeros_like(x), 'k-')
plt.show()
