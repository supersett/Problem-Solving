import sys
n=int(sys.stdin.readline())
data=[]
score=n
for i in range(n):
    a=sys.stdin.readline()
    data.append(a)
for k in data:
    test=list(k)
    for t in test:
        num=test.count(t)
        indexx=test.index(t)
        if num!=1 and test[indexx+num-1]!=t:
            score-=1    
            break
print(score)