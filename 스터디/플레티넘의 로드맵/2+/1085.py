import sys
input=sys.stdin.readline

x,y,w,h=map(int,input().split())

#print(h)

answer=1000

answer=min(w-x,h-y,x,y)
print(answer)


