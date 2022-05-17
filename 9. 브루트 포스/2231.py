import sys
n=int(sys.stdin.readline())
data=[]
def find(x):
    answer=x
    for i in str(x):
        answer+=int(i)
    return answer

for k in range(1,1000001):
    data.append(find(k))

print(data.index(n)+1)