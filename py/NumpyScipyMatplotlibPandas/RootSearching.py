import numpy as np
from scipy import optimize


def fun(x):
    return np.exp(np.exp(x)) - x ** 2


# find zero of fun with initial point 0 by Newton-Raphson
value1 = optimize.newton(fun, 0)
# find zero between (-5, 5) by bisection
value2 = optimize.bisect(fun, -5, 5)
print(value1)
print(value2)
