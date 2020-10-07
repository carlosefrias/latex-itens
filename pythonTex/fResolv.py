from sympy import *
from sympy.abc import *

def fResolvente(a,b,c):
    expr = f"{a}*x**2+{b}*x+{c}"
    print(latex(expr))

fResolvente(2,-2,1)