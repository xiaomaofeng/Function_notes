import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 201)
plt.figure(figsize=(4, 4))
for n in range(2, 5):
    y = x ** (1 / n)
    plt.plot(x, y, label='x^(1/'+str(n)+')')
plt.legend(loc = 'best')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.xlim((-2, 10))
plt.title('Multi-plot e.g. ', fontsize = 18)
plt.show()