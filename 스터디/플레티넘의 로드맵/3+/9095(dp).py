n=int(input().rstrip())
target=[]
for _ in range(n):
    target.append(int(input().rstrip()))

#[ 4 7 10 ]
#4-1=3
#4-2=2
#4-3=1
#dp=[0]*11

def dp_cal(x):
    if x ==1:
        return 1
    elif x==2:
        return 2
    elif x==3:
        return 4
    else:
        return dp_cal(x-1)+dp_cal(x-2)+dp_cal(x-3)

for i in target:
    print(dp_cal(i))
    