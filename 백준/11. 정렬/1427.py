import sys

n=sys.stdin.readline().strip()
target=list(map(int,list(n)))
target.sort(reverse=True)
target2=list(map(str,target))
target3=''.join(target2)
print(target3)

