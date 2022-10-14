import sys

d={}
li=[]
n,m=map(int,sys.stdin.readline().split())

for i in range(1,n+1):
    input=sys.stdin.readline().rstrip()
    d[str(i)]=input
    d[input]=str(i)

for j in range(m):
    ans=sys.stdin.readline().rstrip()
    li.append(d[ans])

for _ in li:
    print(_)
#print(d)
