import sympy as sy

#声明x，y为变量
x = sy.Symbol('x')
y = sy.Symbol('y')
a, b = sy.symbols('a b')

#创建一个新符号（不是函数
f = x**2 + 2 - 2*x + x**2 -1
print(f)
#自动简化
g = x**2 + 2 - 2*x + x**2 -1
print(g)