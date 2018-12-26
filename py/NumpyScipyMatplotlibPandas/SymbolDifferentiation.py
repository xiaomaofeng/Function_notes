import sympy as sy
x =  sy.Symbol( 'x')
y =  sy.Symbol( 'y')
# 单变量 (single variable)
f = sy.cos(x) + x**x
print(sy . diff (f ,  x))
#  多变量  (multi variables)
g = sy.cos(y) * x + sy.log(y)
print(sy.diff (g,  y))