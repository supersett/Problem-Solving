import sys

n=int(sys.stdin.readline())

todo=[]

for x in range(n):
    input_list=list(map(int,sys.stdin.readline().split()))
    input_list.reverse()
    todo.append(input_list)
todo.sort()
print(todo)
time=0
while True:
    sumtime=time
    for x in todo:
        if (time + x[1])<=x[0]:
            time=time+x[1]
        else:
            print(time-1)
            exit()
    time+=1

