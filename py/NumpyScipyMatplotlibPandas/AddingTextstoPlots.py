import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def call(S, K=100, T=0.5, vol=0.6, r=0.05):
    d1 = (np.log(S/K) + (r + 0.5 * vol**2) \
          *T) / np.sqrt(T) / vol
    d2 = (np.log(S/K) + (r - 0.5 * vol**2) \
          *T) / np.sqrt(T) / vol
    return S * norm.cdf(d1) - K * \
    np.exp(-r * T) * norm.cdf(d2)

def delta(S, K=100, T=0.5, vol=0.6, r=0.05):
    d1 = (np.log(S/K) + (r + 0.5 * vol**2)\
          *T) / np.sqrt(T) / vol
    return norm.cdf(d1)
S = np.linspace(40, 161, 100)
fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111)
plt.plot(S,(call(S)-call(100)),'r',lw=1)
plt.plot(100, 0, 'ro', lw=1)
plt.plot(S,np.zeros_like(S), 'black', lw = 1)
plt.plot(S,call(S)-delta(100)*S- \
    (call(100)-delta(100)*100), 'y', lw = 1)
ax.annotate('$\Delta$ hedge', xy=(100, 0), \
            xytext=(110, -10),arrowprops= \
            dict(headwidth =3,width = 0.5, \
            facecolor='black', shrink=0.05))
ax.annotate('Original call', xy= \
            (120,call(120)-call(100)),xytext\
            =(130,call(120)-call(100)),\
            arrowprops=dict(headwidth =10,\
            width = 3, facecolor='cyan', \
            shrink=0.05))
plt.grid(True)
plt.xlim(40, 160)
plt.xlabel('Stock price', fontsize = 18)
plt.ylabel('Profits', fontsize = 18)
plt.show()