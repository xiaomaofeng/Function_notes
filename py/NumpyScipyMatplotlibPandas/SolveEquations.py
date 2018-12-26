import sympy as sy

x  = sy.Symbol ('x')
y  = sy.Symbol('y')

# 给定[-1,1]  (give [-1, 1])
print(sy.solve (x**2 - 1))

# 不能证解决 (no guarantee for solution)
print(sy.solve(x**3  +  0.5*x**2 - 1))

# 用x的表达式表示y     (exepress x in terms of y)
print (sy.solve(x**3  +  y**2))

# 错误：找不到算法 (error:  no  algorithm  can  be  found)
#print(sy.solve(x**x + 2*x - 1))