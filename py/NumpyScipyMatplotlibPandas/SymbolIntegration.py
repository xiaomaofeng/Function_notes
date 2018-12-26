import sympy as sy

x = sy.Symbol('x')
y = sy.Symbol('y')
a = sy.symbols('a')
b = sy.symbols('b')

# 单变量 single  variable
f = sy.sin(x) + sy.exp(x)
y = sy.sin(x)
print(sy.integrate(y, (x, 0, a)))
print(sy.integrate(f, (x, a, b)))
print(sy.integrate(f, (x, 1, 2)))
print(sy.integrate(f, (x, 1.0, 2.0)))
# 多变量 multi variables
g = sy.exp(x) + x * sy.sin(y)
print(sy.integrate(g, (y, a, b)))
