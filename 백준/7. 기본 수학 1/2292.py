import sys
n= int(sys.stdin.readline())
t=1
for i in range(1,n+1):
    if n==1:
        print('1')
        break
    t=t+6*(i-1)
    if t>=n:
        print(i)
        break