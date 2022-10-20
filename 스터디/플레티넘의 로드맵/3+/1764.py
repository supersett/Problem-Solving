n,m=map(int,input().split())

a=set([])
b=set([])

for _ in range(n):
    a.add(input().rstrip())

for _ in range(m):
    b.add(input().rstrip())

c=a&b
list_c=list(c)
list_c.sort()
print(len(list_c))
for i in list_c:
    print(i)