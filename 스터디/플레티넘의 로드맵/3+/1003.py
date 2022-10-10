import sys

n=int(sys.stdin.readline().rstrip())
#d=[0,0]*41
d=[[0 for j in range(2)] for i in range(41)]
d[0]=[1,0]
d[1]=[0,1]
target=[]

def answer(x):
    
    if x==0:
        return d[0]
    if x==1:
        return d[1]

    if d[x]!=[0,0]:
        return d[x]
    else:
        d[x]=[answer(x-1)[0]+answer(x-2)[0],answer(x-1)[1]+answer(x-2)[1]]
        return d[x]

for _ in range(n):
    k=target.append(int(sys.stdin.readline().rstrip()))
    
#print([1,0]+[0,1])

for i in target:
    tt=answer(i)
    print(str(tt[0])+" "+str(tt[1]))
    