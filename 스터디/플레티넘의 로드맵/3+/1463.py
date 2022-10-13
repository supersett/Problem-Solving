from collections import deque
t=int(input())

target=[0 for i in range(t+10)]
#print(target)
#10 5 4 2 1
target[1]=0
target[2]=1
target[3]=1
target[4]=2
target[5]=3
target[6]=2
target[7]=3
target[10]=3

def dp(n):
    k=n
    cnt=0
    if target[n]!=0:
        return cnt+target[n]
    while n!=1:
        if n%3==0:
            n=n/3
            cnt+=1
        elif n%2==0:
            n=n/2
            cnt+=1
        else:
            n-=1
            cnt+=1
    target[k]=cnt
    return cnt

print(dp(t))
#11 10