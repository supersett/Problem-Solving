import sys
n=int(sys.stdin.readline())
data=[]
for x in range(n):
    set=list(map(str,sys.stdin.readline().split()))
    data.append(set)
for i in data:
    want=list(i[0])
    score=0
    p=0
    for j in want:
        if j=='O':
            p+=1
            score+=p
        if j=='X':
            p=0
    print(score)