from asyncio.windows_events import NULL
import sys
n=int(sys.stdin.readline())
data=[]

for a in range(0,1001):
    n=n-5*a
    if n<0:
        break
    if n%3==0:
        if n!=0:
            b=n//3
            data.append(a+b)
        else:
            data.append(a)
print(data)
if len(data)==0:
    print(-1)
else:
    print(min(data))