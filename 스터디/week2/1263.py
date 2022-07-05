import sys

n=int(sys.stdin.readline())

todo=[]

for x in range(n):
    input_list=list(map(int,sys.stdin.readline().split()))
    input_list.reverse()
    todo.append(input_list)
todo.sort()
latest_time=0
latest_time=todo[0][0]-todo[0][1]
time=latest_time
while True:
    for x in range(0,n):
        if (time + todo[x][1])>todo[x][x]:
            latest_time-=1
            break
        else:
            time=time+todo[x][1]
    exit()
if time<=24:
    print(latest_time)
else:
    print('-1')                

