import sys
from sympy import Symbol,solve
import sympy
n=int(sys.stdin.readline().rstrip())
info=sys.stdin.readline().rstrip().replace("[","").replace("]","").replace(',',"")
info_list_string=list(info)
info_int=[]
for x in info_list_string:
    info_int.append(int(x))    
print(info_list_string)
print(info_int)

a=Symbol('a')
b=Symbol('b')

f1=sympy.Eq(a+b,10)
sympy.solve(f1)