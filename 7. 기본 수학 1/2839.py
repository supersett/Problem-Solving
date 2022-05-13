import sys
n=int(sys.stdin.readline())
data=[]
for a in range(0,1001):
    k=n-(5*a)
    if k<0:
        break
    if k%3==0:
        if k==0:
            data.append(a)
        else:
            b=k//3
            data.append(a+b)
if len(data)==0:
    print(-1)
else:
    print(min(data))