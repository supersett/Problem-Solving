import sys
n=int(sys.stdin.readline())
t=n
count=0
while True:
    count+=1
    if n<10:
        a=0
        b=n%10
        i=(b*10)+b        
        n=i
    else:
        a=n//10
        b=n%10
        i=(b*10)+(a+b)%10
        n=i
    if t==i:
        print(count)
        break