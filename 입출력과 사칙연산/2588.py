a=int(input())
b=input()
for x in range(1,len(b)+1):
    print(a*int(b[-x]))
print(a*int(b))