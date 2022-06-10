import sys
n=int(sys.stdin.readline())
for x in range(1,n+1):
    for y in range(x):
        print("*",end="")
    print()
        