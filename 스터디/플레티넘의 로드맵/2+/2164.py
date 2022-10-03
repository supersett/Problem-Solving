from collections import deque

n=int(input())
tar_list=[]

for i in range(1,n+1):
    tar_list.append(i)
    
tar_list=deque(tar_list)

def cal(li):
    while len(li)>1:
        li.popleft()
        li.append(li.popleft())
    print(li[0])


cal(tar_list)
