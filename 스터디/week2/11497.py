import sys
from collections import deque
#절대값 abs(,,)
n=int(sys.stdin.readline())
data=[]

for x in range(n):
    k=int(sys.stdin.readline())
    target=list(map(int,sys.stdin.readline().split()))
    data.append(target)
    
for y in data:
    y.sort(reverse=True)
    new_y=deque(y)
    #print(new_y)
    sorted_list=[]
    new_sorted_list=deque(sorted_list)    
    for i in range(0,len(y)):
        if i%2==0:
            new_sorted_list.appendleft(y[i])
        else:
            new_sorted_list.append(y[i])
    #print(new_sorted_list)
    result_list=list(new_sorted_list)
    #print(result_list)
    target_value_list=[]
    for j in range(0,len(result_list)):
        minus_value=abs(result_list[j-1]-result_list[j])
        target_value_list.append(minus_value)
    print(max(target_value_list))
