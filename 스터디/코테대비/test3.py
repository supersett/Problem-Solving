import sys
from sympy import Symbol,solve
import sympy

a=Symbol('a')
b=Symbol('b')

f1=sympy.Eq(a+b,10)
sympy.solve([f1])