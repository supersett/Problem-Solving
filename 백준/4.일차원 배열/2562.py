import sys
data =[]
for n in range(9):
    a=int(sys.stdin.readline())
    data.append(a)
print(max(data))
print(data.index(max(data))+1)    
