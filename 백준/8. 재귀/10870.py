import sys
n=int(sys.stdin.readline())

def fibo(n):
    result=0
    if n==0:
        result=0
    elif n==1:
        result=1
    else:
        result=fibo(n-1)+fibo(n-2)
    return result
print(fibo(n))